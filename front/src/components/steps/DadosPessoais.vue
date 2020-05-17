<template>
  <div>
    <v-row>
      <v-col cols="3" class="text-center">
        <v-btn
          fab
          color="primary"
          @click="$emit('openDialog')"
        >
          <DefaultAvatar v-if="this.register.avatar"
          :src="this.register.avatar"
          />
        </v-btn>
        <p class="mt-1 mb-0 text-center primary--text">Editar</p>
      </v-col>
      <v-col class=" d-flex justify-start align-center">
        <p class="secondary--text">Adicione uma foto para o seu perfil</p>
      </v-col>
    </v-row>
    <v-form ref="dadospessoais" class="mt-3">
      <v-text-field
        outlined
        label="Nome"
        :rules="[$vln.requiredRule('Nome'), $vln.moreThanRule(2)]"
        required
        v-model="nome"
      ></v-text-field>
      <v-text-field
        outlined
        label="Sobrenome"
        :rules="[$vln.requiredRule('Sobrenome'), $vln.moreThanRule(2)]"
        required
        v-model="sobrenome"
      ></v-text-field>
      <v-text-field
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
            v-model="datanascimento"
            label="Data de nascimento"
            readonly
            v-on="on"
            clearable
            outlined
            :rules="[$vln.requiredRule('Data de nascimento')]"
            @click:clear="datanascimento = null"
          >{{register.datanascimento}}</v-text-field>
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

        outlined
        label="Telefone para contato"
        required
        v-model="telefone"
        v-mask="'(##) #####-####'"
        :rules="[$vln.requiredRule('Telefone'),$vln.foneRule(11)]"
      >{{register.telefone}}</v-text-field>
      <span class="mb-0 grey--text text--darken-2">O número informado tem Whatsapp?</span>
      <v-switch
      v-model="whatsapp"
      class="ma-4" :label="whatsapp ? 'Sim' : 'Não'"></v-switch>

      <v-row justify="space-around">
        <v-col>
          <span class="mb-0 grey--text text--darken-2">Mora sozinho?</span>
          <v-switch
          v-model="moraso"
          class="ma-4" :label="moraso ? 'Sim' : 'Não'"></v-switch>
        </v-col>
        <v-col>
          <span class="mb-0 grey--text text--darken-2">É grupo de risco?</span>
          <v-switch
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
        @click="sendFormData()"
        :loading="register.loginLoading">Próximo</v-btn>
    </v-form>
  </div>
</template>
<script>
import { mapState } from 'vuex';
import DefaultAvatar from '@/components/DefaultAvatar.vue';


export default {
  computed: mapState(['register']),
  components: { DefaultAvatar },
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
      nome: '',
      sobrenome: '',
      cpf: '',
      cpfMask: '###.###.###-##',
      datanascimento: null,
      datanascimentomenu: false,
      telefone: '',
      whatsapp: false,
      moraso: false,
      grupoderisco: false,
    };
  },
  methods: {
    formValidation() {
      return this.$refs.dadospessoais.validate();
    },
    sendFormData() {
      if (this.$refs.dadospessoais.validate()) {
        this.$store.dispatch('register/registerStep1', {
          nome: this.nome,
          sobrenome: this.sobrenome,
          cpf: this.cpf,
          datanascimento: this.datanascimento,
          telefone: this.telefone,
          whatsapp: this.whatsapp,
          moraso: this.moraso,
          grupoderisco: this.grupoderisco,
        });
      }
    },
    saveDate(date) {
      const mdate = new Date(date);
      const dia = mdate.getDay() < 0 ? `0${mdate.getDay()}` : mdate.getDay();
      const mes = (mdate.getMonth() + 1) < 0 ? `0${(mdate.getMonth() + 1)}` : (mdate.getMonth() + 1);
      this.$refs.dpnascimento.save(`${dia}-${mes}-${mdate.getFullYear()}`);
    },
  },
  created() {
    this.nome = this.register.nome ? this.register.nome : '';
    this.sobrenome = this.register.sobrenome ? this.register.sobrenome : '';
    this.email = this.register.email ? this.register.email : '';
    this.cpf = this.register.cpf ? this.register.cpf : '';
    this.datanascimento = this.register.datanascimento ? this.register.datanascimento : '';
    this.telefone = this.register.telefone ? this.register.telefone : '';
    this.whatsapp = this.register.whatsapp;
    this.moraso = this.register.moraso;
    this.grupoderisco = this.register.grupoderisco;
    if (!this.register.avatar) this.$store.dispatch('register/defaultAvatar');
  },
};
</script>
