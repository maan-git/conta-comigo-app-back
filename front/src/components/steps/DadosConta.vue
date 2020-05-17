<template>
  <div>
    <v-form ref="dadosconta" class="mt-3">
      <v-text-field
        outlined
        label="Email"
        required
        :rules="[$vln.requiredRule('E-mail'), $vln.emailRule()]"
        v-model="email"
      ></v-text-field>
      <v-text-field
        outlined
        label="Senha"
        required
        type="password"
        :rules="[$vln.requiredRule('Senha'), $vln.moreThanRule(6)]"
        v-model="password"
        ></v-text-field>
      <v-text-field
        outlined
        label="Repetir Senha"
        required
        type="password"
        :rules="[$vln.requiredRule('Repitir Senha'), $vln.mustBeEqualPass(password),]"
        v-model="repassword"
      ></v-text-field>
      <v-checkbox
        v-model="lieAceito"
        :rules="[$vln.requiredRule('Ler o contrato')]"
        label="Li e aceito os termos de uso do Conta Comigo app"
      ></v-checkbox>
      <v-btn
        block
        rounded
        x-large
        color="primary"
        @click="sendFormData()"
        :loading="register.createUserLoading">Registrar-se</v-btn>
      <p v-if="register.createUserError" class="block text-center mb-0 mt-4 red--text">
        {{register.createUserError}}
      </p>
    </v-form>
  </div>
</template>
<script>
import { mapState } from 'vuex';

export default {
  computed: mapState(['register']),
  watch: {
    email(email) {
      if (email) {
        this.email = email.toLowerCase();
      }
    },
  },
  methods: {
    formValidation() {
      return this.$refs.dadosconta.validate();
    },
    sendFormData() {
      if (this.$refs.dadosconta.validate()) {
        this.$store.dispatch('register/registerStep3', {
          email: this.email,
          password: this.password,
          lieAceito: this.lieAceito,
        });
      }
    },
  },
  data() {
    return {
      username: '',
      email: '',
      password: '',
      repassword: '',
      checkbox: false,
      lieAceito: false,
    };
  },
  created() {
    this.lieAceito = this.register.lieAceito;
  },
};
</script>
