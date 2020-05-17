<template>
  <div>
    <CardContainer>
      <div class="text-center">
        <p class="primary--text font-weight-bold title">Agora é só aguardar!</p>
      </div>

      <v-flex class="how-to">
        <v-img width="350" class="img-center"
               center :src="require('../assets/intro/step1.svg')"></v-img>
        <div class="text-center margin-text">
          <span class="subtitle-1 grey--text">{{text}}</span>
        </div>
      </v-flex>


      <v-btn rounded v-if="!newHelp" class="v-btn v-btn--block v-btn--contained
      v-btn--rounded theme--light v-size--x-large primary">
        OK
      </v-btn>
    </CardContainer>
  </div>
</template>
<script>
import CardContainer from '@/components/CardContainer.vue';

export default {
  components: {
    CardContainer,
  },
  data() {
    return {
      editavel: false,
      // eslint-disable-next-line quotes
      text: `Em breve um voluntário Conta comigo entrará em contato para oferecer ajuda. Continue em casa.`,
    };
  },
};


</script>
<style lang="scss" scoped>
.how-to {
  background-color: white;
  height: 80%;
  width: 70%;
  margin:0 auto;
}
.margin-text{
  margin:12% 0;
}
.img-center{
  margin:0 auto;
}


</style>
