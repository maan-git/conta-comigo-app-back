<template>
  <v-container>
    <HelpForm :newHelp="newHelp"></HelpForm>
    <v-layout mt-5>
      <v-flex xs12 sm6 offset-sm3>
        <v-btn @click="newHelp = !newHelp" >
          {{ newHelp ? 'Visualizar Ajuda' : 'Solicitar Ajuda' }}
        </v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import HelpForm from '@/components/HelpForm.vue';

export default {
  components: {
    HelpForm,
  },
  data() {
    return {
      newHelp: true,
    };
  },
  async beforeCreate() {
    await !this.$store.dispatch('user/getCurrentUser');
  },
};
</script>
