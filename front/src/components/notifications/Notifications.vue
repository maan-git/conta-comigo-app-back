<template>
  <span v-if="show()">
    <v-snackbar v-model="notification" :timeout="0" top
    :color="notification.color ? notification.color: 'secondary'">
      {{notification.description}}
      <v-btn icon color="white"
        @click.native="removeNotification">
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </v-snackbar>
  </span>
</template>
<script>

import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'Notifications',
  computed: mapGetters('notification', {
    notification: 'getVisibleNotification',
  }),
  methods: {
    show() {
      return this.notification !== null;
    },
    ...mapActions('notification', [
      'removeNotification',
    ]),
  },
};
</script>
