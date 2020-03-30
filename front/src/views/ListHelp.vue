<template>
  <v-container>
    <HelpForm v-for="help in helpList"
      :key="help.id_user" :newHelp="newHelp"
      :description="help.description"
      :id_user=help.id_user>
    </HelpForm>
    <v-layout mt-5>
      <v-flex xs12 sm6 offset-sm3>
        <v-btn @click="listHelp()" >
          Listar Ajudas
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
      newHelp: false,
      helpList: [
        { id_user: 'Teste', description: 'Preciso de Ajuda' },
        { id_user: 'VueJs', description: 'Preciso de Ajuda' },
        { id_user: 'Django Libre', description: 'Preciso de Ajuda' }],
    };
  },
  methods: {
    listHelp() {
      this.$store.dispatch('help/list', { });
    },
  },
};
</script>
