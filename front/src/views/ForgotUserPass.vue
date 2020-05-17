<template>
  <div class="login">
    <CardContainer backTo>
      <v-form ref="formForgotUserPass" class="ma-5 text-center"
        @keyup.enter.native="forgotUserPassClick()">
        <p class="primary--text font-weight-medium headline">Recuperar Senha</p>
        <v-text-field
          outlined
          v-model="email"
          label="Email"
          required
          :rules="[$vln.requiredRule('Email')]"
        ></v-text-field>
       <v-btn small class="mt-1" color="primary" to="/login" text>
          <span class="">Login</span>
        </v-btn>
        <v-btn
          class="my-4"
          block
          rounded
          x-large
          @click="forgotUserPassClick()"
          color="primary" :loading="user.forgotUserPassLoading">
          <span class="text-capitalize">Enviar</span>
        </v-btn>
        <v-btn small class="mt-1" color="primary" to="/create-account" text>
          <span class="">Cadastre-se e seja um voluntário</span>
        </v-btn>
        <p v-if="user.forgotUserPassError" class="block text-center mt-4 red--text">
            {{user.forgotUserPassError}}</p>
        <p v-if="user.forgotUserPassSuccess" class="block text-center mt-4 primary--text">
            E-mail de recuperação de senha enviado para <b>{{this.email}}</b>. </p>
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
  watch: {
    email(email) {
      if (email) {
        this.email = email.toLowerCase();
      }
    },
  },
  data() {
    return {
      email: '',
    };
  },
  methods: {
    async forgotUserPassClick() {
      if (this.$refs.formForgotUserPass.validate()) {
        await this.$store.dispatch('user/regeneratePass', { username: this.email });
      }
    },
  },
  created() {
    this.$store.dispatch('register/resetForm');
  },
};
</script>
<style lang="scss" scoped>
.login {
  width: 100%;
  height: 100%;
}
.v-card:not(.v-sheet--tile):not(.v-card--shaped).card-mobile {
  border-radius: 54px;
  justify-self: stretch;
}
</style>
