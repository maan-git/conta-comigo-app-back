<template>
  <v-layout mt-5>
    <v-flex xs12 sm5 offset-sm3>
      <v-card class="pa-5">
        <v-form ref="formLogin" class="ma-5 text-center" >
          <p class="primary--text font-weight-bold title">Login</p>
          <v-text-field
            outlined
            v-model="email.value"
            label="Email"
            required
            :rules="[$vln.requiredRule('Email')]"
          ></v-text-field>
          <v-text-field
            class="mb-0"
            outlined
            v-model="password.value"
            label="Senha"
            type="password"
            required
            :rules="[$vln.requiredRule('Senha')]"
          ></v-text-field>
          <v-btn small class="mb-2" color="primary" to="/" text>
            <span class="">Esqueci a senha</span>
          </v-btn>
          <v-btn
            class="my-4"
            block
            rounded
            x-large
            @click="loginClick()" color="primary" :loading="user.loading">
            <span class="text-capitalize">Entrar</span>
          </v-btn>
          <v-btn small class="mt-1" color="primary" to="/create-account" text>
            <span class="">Cadastre-se e seja um voluntário</span>
          </v-btn>
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
      if (this.$refs.formLogin.validate()) {
        this.$store.dispatch('user/login', { username: this.email, password: this.password });
      }
    },
  },
};
</script>
