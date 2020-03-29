<template>
  <div>
    <CardContainer>
      <v-form ref="formLogin" class="ma-5 text-center" >
        <p class="primary--text font-weight-bold title">Login</p>
        <v-text-field
          outlined
          v-model="email"
          label="Email"
          required
          :rules="[$vln.requiredRule('Email')]"
        ></v-text-field>
        <v-text-field
          class="mb-0"
          outlined
          v-model="password"
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
    </CardContainer>
  </div>
</template>
<script>
import { mapState } from 'vuex';
import CardContainer from '@/components/CardContainer.vue';

export default {
  name: 'Login',
  components: {
    CardContainer,
  },
  computed: mapState(['user']),
  data() {
    return {
      email: '',
      password: '',
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
<style lang="css" scoped>
.card-mobile {
  /* height: 100%; */
  border-bottom: none;
}
.v-card:not(.v-sheet--tile):not(.v-card--shaped).card-mobile {
  border-radius: 54px;
  justify-self: stretch;
}
</style>
