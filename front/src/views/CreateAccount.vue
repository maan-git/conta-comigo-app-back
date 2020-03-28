<template>
  <v-container>
    <UserForm :editavel="editavel"></UserForm>
    <v-layout mt-5>
      <v-flex xs12 sm6 offset-sm3>
        <v-btn @click="editavel = !editavel" >{{ editavel ? 'Editar' : 'Consultar'}}</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import UserForm from '@/components/UserForm.vue';

export default {
  components: {
    UserForm,
  },
  data() {
    return {
      editavel: false,
    };
  },
};
</script>
