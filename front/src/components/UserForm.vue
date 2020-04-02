<template>
  <div>
    <v-stepper alt-labels v-model="e1">
      <v-stepper-header>
        <v-stepper-step step="1">Dados Pessoais</v-stepper-step>

        <!-- <v-divider></v-divider> -->

        <v-stepper-step step="2">Endereço</v-stepper-step>

        <!-- <v-divider></v-divider> -->

        <v-stepper-step step="3">Dados da conta</v-stepper-step>
      </v-stepper-header>
      <v-stepper-items>
        <v-stepper-content step="1">
          <!-- TODO imagem -->
          <v-form ref="steponedata">
            <v-text-field
              :disabled="disapleForm()"
              outlined
              label="Nome"
              :rules="[$vln.requiredRule('Nome'), $vln.moreThanRule(6)]"
              required
              v-model="nome"
            ></v-text-field>
            <v-text-field
              :disabled="disapleForm()"
              outlined
              label="CPF"
              required
              v-model="cpf"
              v-mask="cpfMask"
              :rules="[$vln.requiredRule('CPF'), $vln.cpflRule()]"
            ></v-text-field>
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
                  :rules="[$vln.requiredRule('Data de nascimento')]"
                  @click:clear="datanascimento = null"
                ></v-text-field>
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
              v-mask="'(##) #####-####'"
              :rules="[$vln.requiredRule('Telefone'),$vln.foneRule(11)]"
            ></v-text-field>
            <span class="mb-0 grey--text text--darken-2">O número informado tem Whatsapp?</span>
            <v-switch
            :disabled="disapleForm()"
            v-model="whatsapp"
            class="ma-4" :label="whatsapp ? 'Sim' : 'Não'"></v-switch>

            <v-row justify="space-around">
              <v-col>
                <span class="mb-0 grey--text text--darken-2">Mora sozinho?</span>
                <v-switch
                :disabled="disapleForm()"
                v-model="moraso"
                class="ma-4" :label="moraso ? 'Sim' : 'Não'"></v-switch>
              </v-col>
              <v-col>
                <span class="mb-0 grey--text text--darken-2">É grupo de risco?</span>
                <v-switch
                  :disabled="disapleForm()"
                  v-model="grupoderisco"
                  class="ma-4"
                  :label="grupoderisco ? 'Sim' : 'Não'"></v-switch>
              </v-col>
            </v-row>
            <v-btn
              block
              rounded
              x-large
              color="primary"
              @click="stepOneClick()"
              :loading="user.loading">Próximo</v-btn>
          </v-form>
        </v-stepper-content>
        <v-stepper-content step="2">
          <v-form ref="steptwodata">
            <v-text-field
              :disabled="disapleForm()"
              outlined
              label="Cep"
              v-mask="cepMask"
              :rules="[$vln.requiredRule('Cep')]"
              required
              v-model="cep"
            ></v-text-field>
            <v-text-field
              :disabled="disapleForm()"
              outlined
              label="Endereço"
              :rules="[$vln.requiredRule('Endereço')]"
              required
              v-model="endereco"
            ></v-text-field>
            <v-text-field
              :disabled="disapleForm()"
              outlined
              label="Bairro"
              :rules="[$vln.requiredRule('Bairro')]"
              required
              v-model="bairro"
            ></v-text-field>
            <v-text-field
              :disabled="disapleForm()"
              outlined
              label="Cidade"
              :rules="[$vln.requiredRule('Cidade')]"
              required
              v-model="cidade"
            ></v-text-field>
            <v-text-field
              :disabled="disapleForm()"
              outlined
              label="Estado"
              :rules="[$vln.requiredRule('Estado')]"
              required
              v-model="estado"
            ></v-text-field>
            <v-btn
              block
              rounded
              x-large
              color="primary"
              @click="stepTwoClick()"
              :loading="user.loading">Próximo</v-btn>
          </v-form>
        </v-stepper-content>
        <v-stepper-content step="3">
          <v-form ref="stepthreedata">
            <v-text-field
              :disabled="disapleForm()"
              outlined
              label="Email"
              required
              :rules="[$vln.requiredRule('E-mail'), $vln.emailRule()]"
              v-model="email"
              ></v-text-field>
            <v-text-field
              :disabled="disapleForm()"
              outlined
              label="Senha"
              required
              type="password"
              :rules="[$vln.requiredRule('Senha'), $vln.moreThanRule(6)]"
              v-model="password"
              ></v-text-field>
            <v-text-field
              :disabled="disapleForm()"
              outlined
              label="Repetir Senha"
              required
              type="password"
              :rules="[$vln.requiredRule('Repitir Senha'), $vln.mustBeEqualPass(password),]"
              v-model="repassword"
              ></v-text-field>
              <v-checkbox
                :disabled="disapleForm()"
                v-model="checkbox"
                :rules="[$vln.requiredRule('Ler o contrato')]"
                label="Li e aceito os termos de uso do Conta Comigo app"
              ></v-checkbox>
            <v-btn
              block
              rounded
              x-large
              color="primary"
              @click="stepThreeClick()"
              :loading="user.loading">Registrar-se</v-btn>
          </v-form>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>

    <!-- <v-form ref="userform" class="ma-5" >
        <v-radio-group
          :rules="[$vln.requiredRule('Sexo')]"
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
      <v-btn
        block
        rounded
        x-large
        color="primary"
        @click="createAccount()"
        :loading="user.loading">registrar Usuário</v-btn>
      <p class="mt-4 red--text text-center" v-if="user.loginError">{{user.loginError}}</p>
    </v-form> -->
  </div>
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
    }, // stepper
    steps(val) {
      if (this.e1 > val) {
        this.e1 = val;
      }
    },
    vertical() {
      this.e1 = 2;
      requestAnimationFrame(() => { this.e1 = 1; }); // Workarounds
    },
  },
  data() {
    return {
      nome: '',
      cpf: '',
      cpfMask: '###.###.###-##',
      datanascimento: null,
      datanascimentomenu: false,
      telefone: '',
      whatsapp: false,
      moraso: false,
      grupoderisco: false,

      cep: '',
      cepMask: '#####-###',
      endereco: '',
      bairro: '',
      cidade: '',
      estado: '',

      username: '',
      email: '',
      password: '',
      repassword: '',
      checkbox: false,
      // stepper
      e1: 1,
      steps: 3,
      vertical: false,
      altLabels: false,
      editable: true,
    };
  },
  methods: {
    stepOneClick() {
      if (this.$refs.steponedata.validate()) {
        this.e1 = 2;
      }
    },
    stepTwoClick() {
      if (this.$refs.steptwodata.validate()) {
        this.e1 = 3;
      }
    },
    stepThreeClick() {
      console.log('stepThreeClick()', this.$refs.stepthreedata.validate());
      // this.e1 = 2;
    },

    createAccount() {
      console.log('createAccount', this.$refs.userformum.validate());
      if (this.$refs.userformum.validate()) {
        // this.$store.dispatch('user/register', { email: this.email, password: this.password });
      }
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

    onInput(val) {
      // eslint-disable-next-line radix
      this.steps = parseInt(val);
    },

    nextStep(n) {
      if (n === this.steps) {
        this.e1 = 1;
      } else {
        this.e1 = n + 1;
      }
    },
  },
  created() {
    console.log('created', this.$vln);
  },
};
</script>
<style lang="scss" scoped>
.v-stepper{
  box-shadow: none;
  &__header{
    box-shadow: none;
  }
  &__step {
    flex-basis: 0;
  }
}
</style>
