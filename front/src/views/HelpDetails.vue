<template>
  <div v-if="help.helpDetails">
    <CardContainer backTo title="Detalhes da Ajuda">
      <v-card max-width="400" elevation="0">
        <v-card-title
          class="primary--text"
          v-text="`${help.helpDetails.request_user.first_name},
          ${$filters.calcAge(help.helpDetails.request_user.birth_date)} anos`">
        </v-card-title>
        <v-img
          :src="help.helpDetails.request_user.avatar"
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
        </v-img>
        <v-card-text class="grey--text text--darken-2">
          <div>Criado em {{$filters.formatDate(help.helpDetails.created)}}</div>
          <div>{{help.helpDetails.category.description}}</div>
          <div> Descrição: {{help.helpDetails.description}}</div>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

        <v-btn
          v-if="!isSameUser()"
          :disabled="!!help.helpDetailsDisable"
          @click="applyToHelp()"
          rounded
          :loading="help.helpDetailsLoading"
          block
          color="primary"
          large
        >
          Conta Comigo
          <v-icon right dark>$heart</v-icon>
        </v-btn>
        </v-card-actions>
      </v-card>
    <p v-if="help.helpDetailsError"
       class="block text-center mt-4 red--text">{{help.helpDetailsError}}</p>
    <!-- <p v-if="help.helpDetailsSuccess"
       class="block text-center mt-4 success--text">
      Obrigado <b>{{user.user.first_name}}</b> pela força!</p> -->
    </CardContainer>
  </div>
</template>
<script>

import { mapState } from 'vuex';
import CardContainer from '@/components/CardContainer.vue';


export default {
  components: {
    CardContainer,
  },
  computed: mapState(['help', 'user']),
  data() {
    return { };
  },
  methods: {
    async requestHelp() {
      await this.$store.dispatch('help/getHelp');
    },
    async applyToHelp() {
      await this.$store.dispatch('help/applyToHelpRequest', this.$route.query.id);
    },
    isSameUser() {
      return (this.help.helpDetails.request_user.id === this.user.user.id);
    },
  },
  created() {
    this.$store.dispatch('help/requestHelpDetails', this.$route.query.id);
  },
};
</script>

<style lang="scss" scoped>
</style>
