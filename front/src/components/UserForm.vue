<template>
  <v-layout mt-5>
    <v-flex xs12 sm6 offset-sm3>
      <v-card class="pa-5">
        <h1>User form</h1>
        <v-form ref="userform" class="ma-5" >
          <v-text-field
            :disabled="disapleForm()"
            outlined
            label="Nome"
            :rules="[requiredRule('Nome'), moreThanRule(6)]"
            required
            v-model="nome"
            ></v-text-field>
          <v-text-field
            :disabled="disapleForm()"
            outlined
            label="Email"
            required
            :rules="[requiredRule('E-mail'), emailRule()]"
            v-model="email"
            ></v-text-field>
          <v-text-field
            :disabled="disapleForm()"
            outlined
            label="Senha"
            required
            type="password"
            :rules="[requiredRule('Senha'), moreThanRule(6)]"
            v-model="password"
            ></v-text-field>
          <v-text-field
            :disabled="disapleForm()"
            outlined
            label="CPF"
            required
            v-model="cpf"
            v-mask="cpfMask"
            :rules="[requiredRule('CPF'), cpflRule()]"
            ></v-text-field>

            <v-radio-group
              :rules="[requiredRule('Sexo')]"
              :disabled="disapleForm()"
              v-model="sexo"
              label="Sexo:"
              class="mb-3"
              row>
              <v-radio
                label="Masculino"
                value="m"
              ></v-radio>
              <v-radio
                label="Feminino"
                value="f"
              ></v-radio>
              <v-radio
                label="Não sei"
                value="n/s"
              ></v-radio>
            </v-radio-group>

            <!-- date picker -->
            <v-menu
              ref="dpnascimento"
              v-model="datanascimentomenu"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  :disabled="disapleForm()"
                  v-model="datanascimento"
                  label="Data de nascimento"
                  readonly
                  v-on="on"
                  clearable
                  outlined
                  :rules="[requiredRule('Data de nascimento')]"
                  @click:clear="datanascimento = null"
                ></v-text-field>
                  <!-- prepend-icon="event" -->
              </template>
              <v-date-picker
                ref="picker"
                v-model="datanascimento"
                :max="new Date().toISOString().substr(0, 10)"
                min="1950-01-01"
                @change="saveDate"
              ></v-date-picker>
            </v-menu>
            <!-- date picker -->

          <v-text-field
            :disabled="disapleForm()"
            outlined
            label="Telefone para contato"
            required
            v-model="telefone"
            v-mask="'(##) ####-####'"
            :rules="[requiredRule('Telefone'), foneRule(10)]"></v-text-field>

            <v-row justify="space-around">
              <v-col>
                <span class="mb-0 grey--text text--darken-2">Mora sozinho?</span>
                <v-switch
                :disabled="disapleForm()"
                v-model="moraso"
                class="ma-4" :label="moraso ? 'Sim' : 'Não'"></v-switch>
              </v-col>
              <v-col>
                <span class="mb-0 grey--text text--darken-2">É do grupo de risco?</span>
                <v-switch
                  :disabled="disapleForm()"
                  v-model="grupoderisco"
                  class="ma-4"
                  :label="grupoderisco ? 'Sim' : 'Não'"></v-switch>
              </v-col>
            </v-row>

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
  props: ['editavel'],
  computed: mapState(['user']),
  watch: {
    datanascimentomenu(val) {
      // eslint-disable-next-line no-unused-expressions
      val && setTimeout(() => {
        this.$refs.picker.activePicker = 'YEAR';
      });
    },
  },
  data() {
    return {
      username: '',
      email: '',
      password: '',
      nome: '',
      cpf: '',
      cpfMask: '###.###.###-##',
      sexo: '',
      datanascimento: null,
      datanascimentomenu: false,
      telefone: '',
      moraso: false,
      grupoderisco: false,
    };
  },
  methods: {
    createAccount() {
      if (this.$refs.userform.validate()) {
        this.$store.dispatch('user/register', { email: this.email, password: this.password });
      }
    },

    requiredRule(field) {
      return (v) => !!v || `${field} é obrigatório`;
    },

    lessThanRule(max) {
      return (v) => (v && v.length <= max) || `Tem que ter menos de ${max} caracteres`;
    },
    moreThanRule(min) {
      return (v) => (v && v.length >= min) || `Tem que ter mais de ${min} caracteres`;
    },
    mustHaveNumberRule(num) {
      return (v) => (v && v.length === num) || `Tem que ter ${num} caracteres`;
    },
    foneRule(num) {
      return (v) => {
        const fone = v.replace(/\(/g, '').replace(/\)/g, '').replace(/ /g, '').replace(/-/g, '');
        return (v && fone.length >= num) || `Tem que ter ${num} caracteres`;
      };
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
    saveDate(date) {
      const mdate = new Date(date);
      const dia = mdate.getDay() < 0 ? `0${mdate.getDay()}` : mdate.getDay();
      const mes = (mdate.getMonth() + 1) < 0 ? `0${(mdate.getMonth() + 1)}` : (mdate.getMonth() + 1);
      this.$refs.dpnascimento.save(`${dia}-${mes}-${mdate.getFullYear()}`);
    },
    disapleForm() {
      return this.editavel && !this.user.loading;
    },
  },
};
</script>
