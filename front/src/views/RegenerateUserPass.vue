<template>
  <div class="login">
    <CardContainer backTo>
      <v-form ref="formRegenerateUserPass" class="ma-5 text-center"
        @keyup.enter.native="regenerateUserPassClick()">
        <p class="primary--text font-weight-medium headline">Recuperar Senha</p>
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
        <v-btn
          class="my-4"
          block
          rounded
          x-large
          @click="regenerateUserPassClick()"
          color="primary" :loading="user.forgotUserPassLoading">
          <span class="text-capitalize">Enviar</span>
        </v-btn>
        <p v-if="user.forgotUserPassError" class="block text-center mt-4 red--text">
            {{user.forgotUserPassError}}</p>
        <div v-if="user.forgotUserPassSuccess">
            <p class="block text-center mt-4 primary--text">
                Senha atualizada para o e-mail <b>{{this.email}}</b>. </p>
            <v-btn small class="mt-1" color="primary" to="/login" text>
              <span class="">Login</span>
            </v-btn>
        </div>
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
    async regenerateUserPassClick() {
      // if (this.$refs.formRegenerateUserPass.validate()) { }
    },
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
