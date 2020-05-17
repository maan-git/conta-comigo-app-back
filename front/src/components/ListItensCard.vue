<template>
    <v-container>
        <div v-if="help.helpList">
            <div class="card-info">
                <div>
                    <img width="178" :src="require('../assets/logo_completa.svg')">
                </div>
                <div>
                    <div class="card-description">
                        <label>Nome</label>
                        <span>Pagar Contas na Lotérias</span>
                    </div>
                    <div class="card-date">
                        <span>Nome</span>
                        <br />
                        <span>Está ajudando</span>
                    </div>
                </div>
            </div>
            <div v-if="!accepts" class="card-button">
                <ButtonRouter
                    url='/create-help'
                    text='Conta Comigo'
                    heart=$heart>
                </ButtonRouter>
            </div>
            <div v-if="accepts">
            </div>
        </div>
    </v-container>
</template>

<script>
import { mapState } from 'vuex';
import ButtonRouter from '@/components/ButtonRouter.vue';

export default {
  name: 'ListItensCard',
  props: ['accepts', 'user'],
  computed: mapState(['help']),
  components: {
    ButtonRouter,
  },
  methods: {
    async listHelp() {
      await this.$store.dispatch('help/getHelp', {
        userId: this.user.user.id,
        limit: 10,
        statusId: 1,
      });
    },
  },
};
</script>
<style scoped>
.card-info {
    width: 100%;
    height: 100px;
}
.card-button {
    width: 100%;
    height: 100px;
    position: static;
}
.card-description {
    position: relative;
    float: left;
}
.card-date {
    position: relative;
    float: right;
}
</style>
