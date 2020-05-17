<template>
  <div class="create-help">
    <CardContainer :title="'Preciso de ajuda'">
      <p class="subtitle-1 my-5 px-1 text-center secondary--text">{{txtSub}}</p>
      <v-form class="mt-5" ref="requestform">
        <v-select
          item-text="description"
          item-value="id"
          :items="help.helpCategory"
          label="Tipo de ajuda"
          v-model="requestCategory"
          outlined
          required
          :rules="[$vln.requiredRule('Tipo de ajuda')]"
          :disabled="help.helpRequestSuccess"
        ></v-select>
        <v-textarea
          outlined
          v-model="requestDescription"
          label="Descrição"
          :disabled = "help.helpRequestSuccess"
          :rules="[$vln.requiredRule('Descrição'), $vln.moreThanRule(20)]"
          required
        ></v-textarea>
        <div>
          <p class="body-1 secondary--text px-1">
            Autorizar divulgar número de telefone para todos?
          </p>
          <v-switch
            v-model="divulgarFone"
            class="ma-4"
            :label="divulgarFone ? 'Sim' : 'Não'"></v-switch>
        </div>
        <v-btn
          rounded
          class="mt-5"
          block
          @click="requestHelpSave()"
          :disabled = "help.helpRequestSuccess"
          color="primary" x-large>Procurar voluntário
          <v-icon right dark>$heart</v-icon>
        </v-btn>
        <p
          v-if="help.requestError"
          class="block text-center mt-4 danger--text"
        >{{help.requestError}}</p>
        <!-- <div v-if="help.helpRequestSuccess" class="block text-center mt-4">
          <p class="success--text">
            Solicitação realizada com sucesso!
            <br>Agora é so aguardar que um voluntário irá ajudá-lo.
          </p>
          <v-btn text color="primary" @click="requestHelpNew()">Realizar um novo cadastro</v-btn>
        </div> -->
      </v-form>
    </CardContainer>
  </div>
</template>
<script>
import { mapState } from 'vuex';
import CardContainer from '@/components/CardContainer.vue';

export default {
  name: 'CreateHelp',
  computed: mapState(['help', 'user']),
  components: {
    CardContainer,
  },
  data() {
    return {
      divulgarFone: false,
      requestDescription: '',
      requestCategory: '',
      txtSub: 'Selecione o tipo de ajuda e uma breve descrição do que você precisa e logo um voluntário irá oferecer ajuda.',
    };
  },
  methods: {
    requestHelpSave() {
      if (this.$refs.requestform.validate()) {
        // this.$store.dispatch('notification/showNotification', {
        //   description: 'operação realizada com sucesso',
        //   color: 'success',
        //   id: this.$foos.guid(),
        //   type: 0,
        //   status: 0,
        // });
        this.$store.dispatch('help/requestHelpSave', {
          category: this.requestCategory,
          description: this.requestDescription,
          address_id: this.user.user.addresses[0].id,
          telephone_allowed: this.divulgarFone,
        });
      }
    },
    requestHelpNew() {
      this.requestDescription = null;
      this.$store.dispatch('help/requestHelpNew');
    },
  },
  created() {
    if ((this.description) && (this.category)) {
      this.requestDescription = this.description;
      this.requestCategory = this.category;
    }
    this.$store.dispatch('help/getHelpCategory');
  },
  beforeDestroy() {
    this.$store.dispatch('help/clearHelpState');
  },
};
</script>
<style lang="scss" scoped>
.create-help {
  width: 100%;
  height: 100%;
}
</style>
