<template>
<v-container>
  <h1>HOW TO</h1>
    <!-- :show-arrows="false" -->
  <v-carousel
    :continuous="false"
    :cycle="cycle"
    hide-delimiter-background
    delimiter-icon="mdi-minus"
    height="300"
  >
  <v-carousel-item>
    <v-img width="300" center :src="require('../assets/intro/wiz1.svg')"></v-img>
  </v-carousel-item>
  <v-carousel-item>
    <v-img width="300" :src="require('../assets/intro/wiz2.svg')"></v-img>
  </v-carousel-item>
  <v-carousel-item>
    <v-img width="300" center :src="require('../assets/intro/wiz3.svg')"></v-img>
  </v-carousel-item>
    <!-- <v-carousel-item
      v-for="(slide, i) in slides"
      :key="i"
    >
      <v-sheet
        :color="colors[i]"
        height="100%"
        tile
      >
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <div class="display-3">{{ slide }} Slide</div>
        </v-row>
      </v-sheet>
    </v-carousel-item> -->
  </v-carousel>
</v-container>
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
};
</script>
