<!-- eslint-disable max-len -->
<template>
  <v-flex class="how-to">
    <v-img width="300" center :src="require('../assets/intro/step1.svg')"></v-img>
    <v-img width="300" center :src="require('../assets/intro/step2.svg')"></v-img>
    <v-img width="300" center :src="require('../assets/intro/step3.svg')"></v-img>
  </v-flex>

</template>
<script>
export default {
  data() {
    return {
      colors: [
        'green',
        'secondary',
        'yellow darken-4',
        'red lighten-2',
        'orange darken-1',
      ],
      cycle: false,
      slides: [
        'First',
        'Second',
        'Third',
        'Fourth',
        'Fifth',
      ],
    };
  },
  created() {},
};
</script>
<style lang="scss" scoped>
.how-to {
  background-color: white;
  height: 100%;
}
</style>
