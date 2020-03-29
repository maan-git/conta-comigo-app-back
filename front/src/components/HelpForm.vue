<template>
  <v-layout mt-5>
    <v-flex xs12 sm6 offset-sm3>
      <v-card class="pa-5">
        <v-form class="ma-5" >
          <h1>
            {{newHelp ? "Cadastrar Ajuda" : " Visualizar Ajuda"}}
          </h1>
          <v-chip
            class="ma-2"
            color="primary"
            href="#"
            :active="!newHelp"
            label
          >
            <v-icon left>mdi-account-circle-outline</v-icon>
            {{ id_user }}
          </v-chip>

          <v-select
            :items="categories"
            label="Selecione a Categoria"
            outlined
            required
            :disabled = "!newHelp"
          ></v-select>
          <v-textarea
            outlined
            v-model="description.value"
            label="Descrição"
            :disabled = "!newHelp"
            required
          ></v-textarea>
          <v-btn v-if="newHelp" class="mt-5" block @click="saveHelp()" color="primary">
            Salvar
          </v-btn>
          <v-btn v-if="newHelp" class="mt-5" block @click="saveHelp()" color="primary">
            Editar
          </v-btn>
          <v-btn v-if="!newHelp" class="mt-5" block color="pink">
            <v-icon dark>mdi-heart
          </v-icon>Conta Comigo!</v-btn>
        </v-form>
      </v-card>
    </v-flex>
  </v-layout>
</template>
<script>
import { mapState } from 'vuex';

export default {
  computed: mapState(['help']),
  props: ['newHelp', 'category', 'id_user'],
  data() {
    return {
      categories: [
        { text: 'Passear com Animais' },
        { text: 'Compras' },
        { text: 'Olhar Crianças' },
        { text: 'Outros' },
      ],
      description: { value: '', rules: '' },
    };
  },
  methods: {
    saveHelp() {
      console.log('salvou!');
    },
  },
};
</script>
