<template>
  <div>
    <v-form ref="formemail">
      <v-row class="mt-5 mb-0">
        <v-col :cols="12" class="py-0">
          <v-text-field
            :readonly="!edit"
            outlined
            label="Email"
            disabled
            :rules="[$vln.requiredRule('E-mail'), $vln.emailRule()]"
            v-model="email"
          ></v-text-field>
        </v-col>
      </v-row>
      <p v-if="user.userError"
       class="block text-center mt-4 red--text">{{user.userError}}</p>
    </v-form>
    <v-form ref="formsenha">
      <v-row>
        <v-col :cols="12" class="py-0">
          <v-switch
            color="primary"
            v-model="editPass"
            label="Editar Senha"
          />
        </v-col>
        <v-col :cols="12" class="py-0">
          <v-text-field
            :readonly="!editPass"
            outlined
            label="Senha"
            required
            type="password"
            :rules="[$vln.requiredRule('Senha'), $vln.moreThanRule(6)]"
            v-model="password"
          ></v-text-field>
        </v-col>
        <v-col :cols="12" class="py-0">
          <v-text-field
            :readonly="!editPass"
            outlined
            label="Repetir Senha"
            required
            type="password"
            :rules="[$vln.requiredRule('Repitir Senha'), $vln.mustBeEqualPass(password),]"
            v-model="repassword"
          ></v-text-field>
        </v-col>
      </v-row>
      <p v-if="user.userError"
       class="block text-center mt-4 red--text">{{user.userError}}</p>

      <v-row justify="end" class="px-5" v-if="editPass">
        <v-btn
          large
          color="primary"
          :loading="user.userLoading"
          rounded
          @click="updatePass">Salvar Senha</v-btn>
      </v-row>
    </v-form>
  </div>
</template>
<script>
import { mapState } from 'vuex';

export default {
  name: 'TabPessoal',
  components: {},
  computed: mapState(['user']),
  methods: {
    updateEmail() {
      if (this.$refs.formemail.validate()) {
        this.$store.dispatch('user/updatePersonalData', { email: this.email })
          .then(() => { this.edit = false; });
      }
    },
    updatePass() {
      if (this.$refs.formsenha.validate()) {
        this.$store.dispatch('user/updatePersonalData', { password: this.password })
          .then(() => { this.editPass = false; });
      }
    },
  },
  data() {
    return {
      email: '',
      password: '123456',
      repassword: '123456',
      edit: false,
      editPass: false,
    };
  },
  created() {
    // this.$store.dispatch('user/getUserDetails');
    this.email = this.user.user.email;
  },
};
</script>
