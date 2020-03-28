<template>
  <v-layout mt-5>
    <v-flex xs12 sm6 offset-sm3>
      <v-card class="pa-5">
        <h1>User form</h1>
        <v-form class="ma-5" >
          <v-text-field
            :disabled="editavel"
            outlined
            label="Nome"
            :rules="[]"
            required
            v-model="nome"
            ></v-text-field>
          <v-text-field
            :disabled="editavel"
            outlined
            label="Usuário"
            required
            :rules="[requiredRule('Usuário')]"
            v-model="username"
            ></v-text-field>
          <v-text-field
            :disabled="editavel && !user.loading"
            outlined
            label="Email"
            required
            :rules="[requiredRule('E-mail'), emailRule()]"
            v-model="email"
            ></v-text-field>
          <v-text-field
            :disabled="editavel && !user.loading"
            outlined
            label="Senha"
            required
            type="password"
            :rules="[requiredRule('Senha'), moreThanRule(6)]"
            v-model="password"
            ></v-text-field>
          <v-text-field
            :disabled="editavel"
            outlined
            label="CPF"
            required
            v-model="cpf"
            v-mask="cpfMask"
            :rules="[requiredRule('CPF'), cpflRule()]"
            ></v-text-field>
          <!-- <v-text-field
            outlined
            label="Nome"
            required
            v-model="nome"
            :rules="[requiredRule('')]"></v-text-field> -->
            <v-btn
              block
              color="primary"
              @click="createAccount()"
              :loading="user.loading">registrar Usuário</v-btn>
            <p class="mt-4 red--text text-center" v-if="user.loginError">{{user.loginError}}</p>
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
      username: '',
      email: '',
      password: '',
      nome: '',
      cpf: '',
      cpfMask: '###.###.###-##',
      sexo: '',
      datanascimento: '',
      telefone: '',
      moraso: false,
      grupoderisco: false,
    };
  },
  methods: {
    createAccount() {
      this.$store.dispatch('user/register', { email: this.email, password: this.password });
    },

    requiredRule(field) {
      return (v) => !!v || `${field} é obrigatório`;
    },

    lessThanRule(max) {
      return (v) => (v && v.length <= max) || `Must be less than ${max} characters`;
    },
    moreThanRule(min) {
      return (v) => (v && v.length >= min) || `Must be more than ${min} characters`;
    },
    emailRule() {
      return (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid';
    },
    cpflRule() {
      return (v) => {
        const erroMsg = 'CPF não valido';
        // eslint-disable-next-line no-useless-escape
        const strCPF = v.replace(/\./g, '').replace(/-/g, '');
        let Soma = 0;
        let Resto = 0;
        Soma = 0;
        if (strCPF === '00000000000') { return erroMsg; }

        // eslint-disable-next-line no-plusplus
        for (let i = 1; i <= 9; i++) {
          // eslint-disable-next-line radix
          Soma += parseInt(strCPF.substring(i - 1, i)) * (11 - i);
        }
        Resto = (Soma * 10) % 11;

        if ((Resto === 10) || (Resto === 11)) Resto = 0;
        // eslint-disable-next-line radix
        if (Resto !== parseInt(strCPF.substring(9, 10))) { return erroMsg; }

        Soma = 0;
        // eslint-disable-next-line no-plusplus
        for (let i = 1; i <= 10; i++) {
          // eslint-disable-next-line radix
          Soma += parseInt(strCPF.substring(i - 1, i)) * (12 - i);
        }
        Resto = (Soma * 10) % 11;

        if ((Resto === 10) || (Resto === 11)) Resto = 0;
        // eslint-disable-next-line radix
        if (Resto !== parseInt(strCPF.substring(10, 11))) { return erroMsg; }
        return true;
      };
    },
  },
};
</script>
