<template>
  <v-layout mt-5>
    <v-flex xs12 sm6 offset-sm3>
      <v-card class="pa-5">
        <v-form class="ma-5" >
          <v-text-field
            outlined
            v-model="email.value"
            label="Usuário"
            required
          ></v-text-field>
          <v-text-field
            outlined
            v-model="password.value"
            label="Senha"
            type="password"
            required
          ></v-text-field>
          <v-btn block @click="loginClick()" color="primary" :loading="user.loading">login</v-btn>
          <p v-if="user.loginError" class="block text-center mt-4">{{user.loginError}}</p>
        </v-form>
      </v-card>
    </v-flex>
  </v-layout>
</template>
<script>
import { mapState } from 'vuex';

export default {
  computed: mapState(['user']),
  data() {
    return {
      email: { value: '', rules: '' },
      password: { value: '', rules: '' },
    };
  },
  methods: {
    loginClick() {
      this.$store.dispatch('user/login', { email: this.email, password: this.password });
    },
  },
};
</script>
