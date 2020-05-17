<template>
  <v-navigation-drawer
      v-model="drawer"
      absolute
      :color="'#532594'"
    >
      <v-list nav dense>
        <v-btn @click="toogleMenu()" x-large icon color="white">
          <v-icon>mdi-close</v-icon>
        </v-btn>
        <v-list-item-group active-class="deep-purple--text text--accent-4">
          <v-list-item @click="linkClick('/')" >
            <v-img :max-width="500" :src="require('../assets/logo_completa.svg')"></v-img>
          </v-list-item>
          <v-btn
            color="primary"
            block
            right
            elevation="0"
            @click="linkClick('/user-details')"
            >Perfil</v-btn>
          <v-btn
            color="primary"
            block
            right
            elevation="0"
            @click="linkClick('/requested-helps-user')"
          >Meus pedidos</v-btn>
          <v-btn
            color="primary"
            block
            right
            elevation="0"
            @click="logout()">Logout</v-btn>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
</template>
<script>
// import notificationClient from '../plugins/NotificationClient';

export default {
  data() { return { drawer: false }; },
  methods: {
    toogleMenu() {
      this.drawer = !this.drawer;
    },
    linkClick(to) {
      this.toogleMenu();
      this.$router.push({ path: to });
    },
    logout() {
      this.toogleMenu();
      this.$store.dispatch('user/logout').then(() => {
        // notificationClient.stopListening();
        this.$router.push({ path: '/login' });
      });
    },
  },
};
</script>
<style lang="scss" scoped>
.v-navigation-drawer--absolute {
  z-index: 10000;
}
</style>
