<template>
  <v-layout mt-5>
    <v-flex xs12 sm6 offset-sm3>
      <v-card class="pa-5">
        <h1>User form</h1>
        <v-form class="ma-5" >
          <!-- <v-text-field
            :disabled="editavel"
            outlined
            label="Usuário"
            required
            v-model="username.value"
            ></v-text-field> -->
            <!-- :rules="username.rules" -->
          <v-text-field
            :disabled="editavel && !user.loading"
            outlined
            label="Email"
            required
            v-model="email.value"
            ></v-text-field>
            <!-- :rules="email.rules" -->
          <v-text-field
            :disabled="editavel && !user.loading"
            outlined
            label="Senha"
            required
            type="password"
            v-model="password.value"
            ></v-text-field>
            <!-- :rules="password.rules" -->
          <!-- <v-text-field
            :disabled="editavel"
            outlined
            label="Nome"
            required
            v-model="nome.value"
            ></v-text-field> -->
            <!-- :rules="nome.rules" -->
          <!-- <v-text-field
            :disabled="editavel"
            outlined
            label="CPF"
            required
            v-model="cpf.value"
            ></v-text-field> -->
            <!-- :rules="cpf.rules" -->
          <!-- <v-text-field
            outlined
            label="Nome"
            required
            v-model="nome.value"
            :rules="nome.rules"></v-text-field> -->
            <v-btn
              block
              color="primary"
              @click="createAccount()"
              :loading="user.loading">registrar Usuário</v-btn>
            <!-- <p v-if="user.loginError">{{loginError}}</p> -->
        </v-form>
      </v-card>
    </v-flex>
  </v-layout>
</template>
<script>

import { mapState } from 'vuex';

export default {
  computed: mapState(['user']),
  props: ['editavel'],
  data() {
    return {
      username: {
        value: '',
        rules: '',
      },
      email: {
        value: '',
        rules: '',
      },
      password: {
        value: '',
        rules: '',
      },
      nome: {
        value: '',
        rules: '',
      },
      cpf: {
        value: '',
        rules: '',
      },
      sexo: {
        value: {
          val1: 'masculino',
          val2: 'feminino',
        },
        rules: '',
      },
      datanascimento: {
        value: '',
        rules: '',
      },
      telefone: {
        value: '',
        rules: '',
      },
      moraso: {
        value: false,
        rules: '',
      },
      grupoderisco: {
        value: false,
        rules: '',
      },
    };
  },
  methods: {
    createAccount() {
      this.$store.dispatch('user/register', { email: this.email.value, password: this.password.value });
    },
  },
};
</script>
