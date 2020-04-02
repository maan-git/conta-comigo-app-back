<template>
  <v-container>
    <div v-if="help.helpList">
      <HelpForm v-for="help in help.helpList"
        :key="help.id_user" :newHelp="newHelp"
        :description="help.description"
        :id_user=help.id_user>
      </HelpForm>
    </div>
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
import { mapState } from 'vuex';
import HelpForm from '@/components/HelpForm.vue';

export default {
  components: {
    HelpForm,
  },
  computed: mapState(['help']),
  data() {
    return {
      newHelp: false,
    };
  },
  async beforeCreate() {
    await !this.$store.dispatch('user/getCurrentUser');
  },
  methods: {
    async listHelp() {
      await this.$store.dispatch('help/listHelp');
    },
  },
};
</script>
