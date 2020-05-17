<template>
  <div>
    <v-form ref="enderecoform">
      <v-row justify="end" class="mb-0 pa-4">
        <v-switch
          color="primary"
          v-model="edit"
          label="Editar"
        />
      </v-row>
      <v-row class="mb-0">
        <v-col :cols="12" class="py-0">
          <v-text-field
            :readonly="!edit"
            outlined
            label="Cep"
            v-mask="cepMask"
            :rules="[$vln.requiredRule('Cep')]"
            required
            v-model="cep"
          ></v-text-field>
        </v-col>
        <v-col :cols="12" class="py-0">
          <v-text-field
            :readonly="!edit"
            outlined
            label="Endereço"
            :rules="[$vln.requiredRule('Endereço')]"
            required
            v-model="endereco"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col :cols="12" class="py-0">
          <v-select
            :readonly="(bairros.length <= 1)"
            item-value="id"
            item-text="description"
            :items="address.bairros"
            v-model="bairro"
            outlined
            menu-props="auto"
            label="Bairro"
            :rules="[$vln.requiredRule('Bairro')]"
            required
          ></v-select>
        </v-col>
        <v-col :cols="12" class="py-0">
          <v-text-field
            :readonly="true"
            outlined
            label="Cidade"
            :rules="[$vln.requiredRule('Cidade')]"
            required
            v-model="cidade"
          ></v-text-field>
        </v-col>
        <v-col class="py-0">
          <v-text-field
            :readonly="true"
            outlined
            label="Estado"
            :rules="[$vln.requiredRule('Estado')]"
            required
            v-model="estado"
          ></v-text-field>
        </v-col>
      </v-row>
      <p v-if="user.userError"
       class="block text-center mt-4 red--text">{{user.userError}}</p>
      <v-row justify="end" class="px-5" v-if="edit">
        <v-btn
          large
          color="primary"
          rounded
          :loading="user.userLoading"
          @click="updateData"
        >Salvar</v-btn>
      </v-row>
    </v-form>
  </div>
</template>
<script>
import { mapState } from 'vuex';

export default {
  name: 'TabPessoal',
  components: {},
  computed: mapState(['user', 'address']),
  watch: {
    cep(cep) {
      if (cep && cep.length === 9) {
        this.$store.dispatch('address/findByZip', cep);
      }
    },
  },
  methods: {
    resetData() {
      this.edit = false;
    },
    updateData() {
      if (this.$refs.enderecoform.validate()) {
        const cep = this.cep.replace(/-/g, '');
        const data = {
          user_address_id: this.user.user.addresses[0].id,
          neighborhood_id: this.bairro,
          address: this.endereco,
          zip: cep,
        };
        this.$store.dispatch('user/updateAddress', data)
          .then(() => { this.edit = false; });
      }
    },
  },
  data() {
    return {
      cep: '',
      cepMask: '#####-###',
      endereco: '',
      bairro: '',
      bairros: [],
      cidade: '',
      estado: '',
      edit: false,
    };
  },
  created() {
    this.cep = this.user.user.addresses[0].zip_code;
    this.endereco = this.user.user.addresses[0].address;

    this.$store.watch(
      (state) => state.address,
      (val) => {
        if (this.endereco !== val.endereco && this.edit) this.endereco = val.endereco;
        if (this.bairros !== val.bairros) this.bairro = val.bairro;
        if (this.cidade !== val.cidade) this.cidade = val.cidade;
        if (this.estado !== val.estado) this.estado = val.estado;
      }, { deep: true },
    );
  },
};
</script>
