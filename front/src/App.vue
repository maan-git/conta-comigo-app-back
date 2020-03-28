<template>
  <v-app>
    <NavBar/>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue';
import NavBar from './components/NavBar.vue';

export default {
  name: 'App',

  components: {
    // HelloWorld,
    NavBar,
  },

  data: () => ({
    //
  }),
};
</script>
