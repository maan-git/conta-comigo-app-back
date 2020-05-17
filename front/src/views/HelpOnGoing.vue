<!--eslint-disable max-len-->
<template>
  <div v-if="help.helpDetails">
    <CardContainer backTo :title="'Detalhes da Ajuda'">
      <v-card max-width="400" elevation="0">
        <v-card-title
          class="primary--text"
        >
        <!-- v-text="`${help.helpDetails.helping_users[0].helper_user.first_name} ${help.helpDetails.helping_users[0].helper_user.last_name}, ${$filters.calcAge(help.helpDetails.helping_users[0].helper_user.birth_date)} anos`" -->
          <div class="title">{{help.helpDetails.category.description}}</div>
          <div class="subtitle-1">{{help.helpDetails.description}}</div>
        </v-card-title>
        <!-- <v-img
          :src="help.helpDetails.helping_users[0].helper_user.avatar"
        >
          <template v-slot:placeholder>
            <v-row
              class="fill-height ma-0"
              align="center"
              justify="center"
            >
              <v-progress-circular indeterminate color="danger"></v-progress-circular>
            </v-row>
          </template>
        </v-img> -->
        <v-card-text class="grey--text text--darken-2">
          <!-- <div class="subtitle-3 mb-0 mt-2">Solicitante:</div> -->
          <div class="d-flex align-center">
            <DefaultAvatar
              :size="70"
              :src="help.helpDetails.request_user.avatar"/>
            <div class="subtitle-1 font-weight-bold ml-2 mt-1">{{help.helpDetails.request_user.first_name}} {{help.helpDetails.request_user.last_name}}, {{$filters.calcAge(help.helpDetails.request_user.birth_date)}} anos</div>
          </div>
        </v-card-text>

        <v-card-text>
          <div class="voluntario">
            <div class="d-flex align-center">
              <div class="subtitle-1 font-weight-bold mr-2 mt-1 text-right">
                {{help.helpDetails.helping_users[0].helper_user.first_name}} {{help.helpDetails.helping_users[0].helper_user.last_name}}, {{$filters.calcAge(help.helpDetails.helping_users[0].helper_user.birth_date)}} anos
                <div class="caption mb-0">Ajudando</div>
              </div>
              <DefaultAvatar
                :size="70"
                :src="help.helpDetails.helping_users[0].helper_user.avatar"/>
            </div>
            <div class="d-flex justify-space-around mt-3">
              <v-btn  icon large color="primary" target="_blank"
                :href="`mailto:${help.helpDetails.helping_users[0].helper_user.email}`"
              >
                <v-icon>mdi-email</v-icon>
                <!-- <span class="subtitle-2">{{help.helpDetails.helping_users[0].helper_user.email}}</span> -->
              </v-btn>
              <v-btn icon large color="primary" :href="`callto:${help.helpDetails.helping_users[0].helper_user.phone_number}`" target="_blank">
                <!-- <span class="subtitle-2">{{help.helpDetails.helping_users[0].helper_user.phone_number}}</span> -->
                <v-icon>mdi-phone</v-icon>
              </v-btn>

              <v-btn icon large color="primary" :href="`https://wa.me/${help.helpDetails.helping_users[0].helper_user.phone_number}`" target="_blank">
                <v-icon>mdi-whatsapp</v-icon>
              </v-btn>
            </div>
          </div>
            <!--  -->
        </v-card-text>
        <v-card-actions v-if="help.helpDetails">
          <!-- <v-spacer></v-spacer> -->
          <v-btn
            block
            large
            @click="opencancelDialog()"
            rounded v-if="!(help.helpDetails.status.id === 99)"
            :disabled="!!help.helpDetailsDisable"
            :loading="help.helpDetailsLoading"
            color="danger"
          >
            <span class="white--text font-weight-bold">
              Cancelar
            </span>
          </v-btn>
        </v-card-actions>
      </v-card>
    <!-- <p v-if="help.helpDetailsError"
       class="block text-center mt-4 red--text">{{help.helpDetailsError}}</p>
    <p v-if="help.helpDetailsSuccess"
       class="block text-center mt-4 success--text">
      Obrigado <b>{{user.user.first_name}}</b> pela força!</p> -->
    </CardContainer>


    <v-dialog
      v-model="dialog"
      max-width="300"
    >
      <v-card>
        <v-card-title>
          <p class="title">Você tem certeza que deseja cancelar a ajuda?</p>
        </v-card-title>

        <v-card-text>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="success"
            @click="dialog = false"
            rounded
            :disabled="help.helpLoading"
          >
            <span class="white--text font-weight-bold">
              Não
            </span>
          </v-btn>

          <v-btn
            color="danger"
            @click="cancelHelp()"
            rounded
            :loading="help.helpLoading"
          >
          <span class="white--text font-weight-bold">
            Sim
          </span>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </div>
</template>
<script>

import { mapState } from 'vuex';
import CardContainer from '@/components/CardContainer.vue';
import DefaultAvatar from '@/components/DefaultAvatar.vue';


export default {
  components: {
    CardContainer,
    DefaultAvatar,
  },
  computed: mapState(['help', 'user']),
  data() {
    return {
      dialog: false,
    };
  },
  methods: {
    async requestHelp() {
      await this.$store.dispatch('help/getHelp');
    },
    async applyToHelp() {
      await this.$store.dispatch('help/applyToHelpRequest', this.$route.query.id);
    },
    opencancelDialog() {
      this.dialog = true;
    },
    cancelHelp() {
      this.$store.dispatch('help/cancelHelp', this.$route.query.id);
    },
  },
  created() {
    this.$store.dispatch('help/requestHelpDetails', this.$route.query.id);
  },
};
</script>

<style lang="scss" scoped>
.voluntario {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}
</style>
