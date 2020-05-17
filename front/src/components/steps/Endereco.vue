<template>
  <div>
    <v-form ref="enderecoform" class="mt-3">
      <v-text-field
        outlined
        label="Cep"
        v-mask="cepMask"
        :rules="[$vln.requiredRule('Cep')]"
        required
        v-model="cep"
      ></v-text-field>
      <v-text-field
        outlined
        label="Endereço"
        :rules="[$vln.requiredRule('Endereço')]"
        required
        v-model="endereco"
      ></v-text-field>
      <v-select
        item-value="id"
        item-text="description"
        :items="address.bairros"
        v-model="bairro"
        :readonly="address.bairros.length <= 1"
        outlined
        menu-props="auto"
        label="Bairro"
        :rules="[$vln.requiredRule('Bairro')]"
        required
      ></v-select>

      <v-text-field
        :readonly="true"
        outlined
        label="Cidade"
        :rules="[$vln.requiredRule('Cidade')]"
        required
        v-model="cidade"
      ></v-text-field>

      <v-text-field
        :readonly="true"
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
        @click="sendFormData()"
        :loading="address.createUserLoading">Próximo</v-btn>
      <p v-if="address.createUserError" class="block text-center mb-0 mt-4 red--text">
        {{address.createUserError}}
      </p>
    </v-form>
  </div>
</template>
<script>
import { mapState } from 'vuex';

export default {
  computed: mapState(['address']),
  watch: {
    cep(cep) {
      if (cep.length === 9) {
        this.$store.dispatch('address/findByZip', cep);
      }
    },
  },
  data() {
    return {
      cep: '',
      cepMask: '#####-###',
      endereco: '',
      bairro: '',
      cidade: '',
      estado: '',
    };
  },
  methods: {
    formValidation() {
      return this.$refs.enderecoform.validate();
    },
    sendFormData() {
      if (this.$refs.enderecoform.validate()) {
        this.$store.dispatch('register/setStep', 3);
      }
    },
  },
  created() {
    this.cep = this.address.cep ? this.address.cep : '';
    this.endereco = this.address.endereco ? this.address.endereco : '';
    this.bairro = this.address.bairro ? this.address.bairro : '';
    this.cidade = this.address.cidade ? this.address.cidade : '';
    this.estado = this.address.estado ? this.address.estado : '';

    this.$store.watch(
      (state) => state.address,
      (val) => {
        if (this.endereco !== val.endereco) this.endereco = val.endereco;
        if (this.bairros !== val.bairros) this.bairro = val.bairro;
        if (this.cidade !== val.cidade) this.cidade = val.cidade;
        if (this.estado !== val.estado) this.estado = val.estado;
      }, { deep: true },
    );
  },
};
</script>
