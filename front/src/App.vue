<template>
  <v-app :class="purple()">
    <!--  -->
    <SideMenu ref="sidemenu"/>
    <NavBar v-on:toogle="toogleMenu()"/>
    <v-content class="content-width">
      <router-view></router-view>
    </v-content>
    <Notifications />
    <v-btn v-scroll="onScroll" v-show="fab" fab
      dark fixed bottom right color="danger" @click="toTop"
    ><v-icon>mdi-arrow-up</v-icon></v-btn>
  </v-app>
</template>

<script>
import { mapState } from 'vuex';
import NavBar from './components/NavBar.vue';
import Notifications from './components/notifications/Notifications.vue';
import SideMenu from './components/SideMenu.vue';

export default {
  name: 'App',
  components: {
    NavBar,
    SideMenu,
    Notifications,
  },
  computed: mapState(['user', 'notification']),
  data: () => ({
    fab: false,
  }),
  methods: {
    purple() {
      if (this.$router.history.current.name !== 'Home') {
        return 'purple';
      }
      return '';
    },
    toogleMenu() {
      this.$refs.sidemenu.toogleMenu();
    },
    onScroll(e) {
      if (typeof window === 'undefined') return;
      const top = window.pageYOffset || e.target.scrollTop || 0;
      this.fab = top > 20;
    },
    toTop() {
      this.$vuetify.goTo(0);
    },
  },
};
</script>
<style lang="scss" scoped>
.theme--light.purple {
  background-color: #532594;
  background-image: url('./assets/pattern.svg');
  transition: all .3s ease-in-out;
}
.content-width {
  width: 100%;
  max-width: 1000px;
  align-self: center;
}
</style>
