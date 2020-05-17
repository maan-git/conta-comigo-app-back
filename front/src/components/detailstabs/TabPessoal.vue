<template>
  <div>
    <v-form ref="pessoalform">
      <v-row justify="space-between" class="mb-0 pa-4">
        <v-btn
          large
          fab
          color="primary"
          :disabled="!edit"
          @click="$refs.dialog.open()"
        >
          <DefaultAvatar :src="avatar" :size="56"/>
        </v-btn>
        <v-switch
          color="primary"
          v-model="edit"
          label="Editar"
        />
      </v-row>
      <v-row class="mb-0">
        <v-col :cols="12" :sm="6" class="py-0">
          <v-text-field
            :readonly="!edit"
            outlined
            label="Nome"
            required
            :rules="[$vln.requiredRule('Nome'), $vln.moreThanRule(2)]"
            v-model="first_name"
          ></v-text-field>
        </v-col>
        <v-col :cols="12" :sm="6" class="py-0">
          <v-text-field
            :readonly="!edit"
            outlined
            label="Sobrenome"
            required
            :rules="[$vln.requiredRule('Sobrenome'), $vln.moreThanRule(2)]"
            v-model="last_name"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col :cols="12" :sm="6" class="py-0">
          <v-text-field
            :readonly="!edit"
            outlined
            label="CPF"
            disabled
            v-model="cpf"
            v-mask="'###.###.###-##'"
            :rules="[$vln.requiredRule('CPF'), $vln.cpflRule()]"
          ></v-text-field>
        </v-col>
        <v-col :cols="12" :sm="6" class="py-0">
          <v-menu
            :disabled="!edit"
            ref="dpnascimento"
            v-model="datanascimentomenu"
            :close-on-content-click="false"
            transition="scale-transition"
            offset-y
            min-width="290px"
          >
            <template v-slot:activator="{ on }">
              <v-text-field
                v-model="birth_date"
                label="Data de nascimento"
                readonly
                v-on="on"
                clearable
                outlined
                :rules="[$vln.requiredRule('Data de nascimento')]"
                @click:clear="birth_date = null"
              >{{birth_date}}</v-text-field>
            </template>
            <v-date-picker
              ref="picker"
              v-model="birth_date"
              :max="new Date().toISOString().substr(0, 10)"
              min="1950-01-01"
              @change="saveDate"
            ></v-date-picker>
          </v-menu>
        </v-col>
        <v-col :cols="8"  class="py-0">
          <v-text-field
            :readonly="!edit"
            outlined
            label="Telefone para contato"
            required
            v-model="phone_number"
            v-mask="'(##) #####-####'"
            :rules="[$vln.requiredRule('Telefone'),$vln.foneRule(11)]"
          ></v-text-field>
        </v-col>
        <v-col class="py-0">
          <v-checkbox class=" pt-0"
            :readonly="!edit"
            v-model="is_phone_whatsapp" label=" " prepend-icon="mdi-whatsapp"
            ></v-checkbox>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="py-0 pr-0">
          <v-checkbox class="mt-0 pt-0"
            :readonly="!edit"
            v-model="live_alone"
            :label="'Mora só'"></v-checkbox>
        </v-col>
        <v-col class="py-0 pl-0">
          <v-checkbox class="mt-0 pt-0"
            :readonly="!edit"
            v-model="is_at_risk_group"
            :label="'Grupo de risco'"></v-checkbox>
        </v-col>
      </v-row>
      <p v-if="user.userError"
       class="block text-center mt-4 red--text">{{user.userError}}</p>
      <v-row justify="end" class="px-5" v-if="edit">
        <v-btn
          large
          color="primary"
          :loading="user.userLoading"
          rounded
          @click="updateData">Salvar</v-btn>
      </v-row>
    </v-form>
    <CropDialog ref="dialog" v-on:avatar="avatar = $event" />
  </div>
</template>
<script>
import { mapState } from 'vuex';
import DefaultAvatar from '@/components/DefaultAvatar.vue';
import CropDialog from '@/components/CropDialog.vue';

export default {
  name: 'TabPessoal',
  components: {
    DefaultAvatar, CropDialog,
  },
  computed: mapState(['user']),
  methods: {
    saveDate(date) {
      const mdate = new Date(date);
      const dia = mdate.getDay() < 0 ? `0${mdate.getDay()}` : mdate.getDay();
      const mes = (mdate.getMonth() + 1) < 0 ? `0${(mdate.getMonth() + 1)}` : (mdate.getMonth() + 1);
      this.$refs.dpnascimento.save(`${dia}-${mes}-${mdate.getFullYear()}`);
    },
    updateData() {
      // password: string,
      // email: string,
      // is_superuser: true,
      if (this.$refs.pessoalform.validate()) {
        const phone = `+55${this.phone_number.replace(/\(/g, '').replace(/\)/g, '').replace(/ /g, '').replace(/-/g, '')}`;
        const cpf = this.cpf.replace(/\./g, '').replace(/-/g, '');
        // eslint-disable-next-line prefer-const
        let data;
        const mockdata = {
          first_name: this.first_name,
          last_name: this.last_name,
          cpf,
          birth_date: this.birth_date,
          phone_number: phone,
          is_phone_whatsapp: this.is_phone_whatsapp,
          is_at_risk_group: this.is_at_risk_group,
          live_alone: this.live_alone,
        };
        if (this.avatar !== this.user.user.avatar) {
          data = { avatar: this.avatar, ...mockdata };
        } else {
          data = mockdata;
        }
        this.$store.dispatch('user/updatePersonalData', data)
          .then(() => { this.edit = false; });
      }
    },
    resetData() {
      this.edit = false;
    },
  },
  data() {
    return {
      avatar: null,
      first_name: '',
      last_name: '',
      phone_number: '',
      cpf: '',
      cpfMask: '###.###.###-##',
      birth_date: null,
      datanascimentomenu: false,
      is_phone_whatsapp: false,
      is_at_risk_group: false,
      live_alone: false,
      edit: false,
    };
  },
  created() {
    // this.$store.dispatch('user/getUserDetails');
    this.avatar = this.user.user.avatar;
    this.first_name = this.user.user.first_name;
    this.last_name = this.user.user.last_name;
    this.cpf = this.user.user.cpf;
    this.birth_date = this.user.user.birth_date;
    this.phone_number = String(this.user.user.phone_number).substr(3);
    this.is_phone_whatsapp = this.user.user.is_phone_whatsapp;
    this.is_at_risk_group = this.user.user.is_at_risk_group;
    this.live_alone = this.user.user.live_alone;
  },
};
</script>
