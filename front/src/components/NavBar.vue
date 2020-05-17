<template>
  <v-app-bar v-if="user.user" app color="primary" dark prominent dense>
    <div class="nav-container">
      <v-btn icon fab large @click="$emit('toogle')">
        <v-img
          alt="conta comigo"
          class="shrink "
          contain
          :src="require('../assets/icone.svg')"
          transition="scale-transition"
          width="45"
        >
          <template v-slot:placeholder>
            <v-row
              class="fill-height ma-0"
              align="center"
              justify="center"
            >
              <v-progress-circular indeterminate color="danger"></v-progress-circular>
            </v-row>
          </template>
        </v-img>
      </v-btn>
      <div class="nav-container__text">
        <p class="title mb-0">Olá, {{user.user.first_name}}
          <br>
          <span class="subtitle-1">Conta comigo!</span>
        </p>
      </div>

      <DefaultAvatar :src="user.user.avatar"/>
    </div>
  </v-app-bar>
</template>
<script>

import { mapState } from 'vuex';
import DefaultAvatar from '@/components/DefaultAvatar.vue';
// import notificationClient from '../plugins/NotificationClient';

export default {
  name: 'NavBar',
  components: { DefaultAvatar },
  computed: mapState(['user']),
  methods: {
    logout() {
      this.$store.dispatch('user/logout').then(() => {
        // notificationClient.stopListening();
        this.$router.push('/login');
      });
    },
  },
};
</script>
<style lang="scss" scoped>
.v-toolbar {
  border-bottom-right-radius: 40px;
  border-bottom-left-radius: 40px;
  max-width: 1200px;
  margin: 0 auto;
}

.nav-container {
  width: 90%;
  height: 60px;
  margin: 10px auto 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  &__text {
    text-align: center;
    vertical-align: middle;
  }
}

</style>
