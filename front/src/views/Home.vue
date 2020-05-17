<template>
  <v-container class="home" @load="listHelp()">
    <ListHelp/>
    <ListVolunteers/>
  </v-container>
</template>

<script>
// @ is an alias to /src
import { mapState } from 'vuex';
import ListHelp from '@/components/ListHelp.vue';
import ListVolunteers from '@/components/ListVolunteers.vue';

export default {
  name: 'Home',
  components: {
    ListHelp,
    ListVolunteers,
  },
  computed: mapState(['help', 'user']),
  methods: {
    async listHelp() {
      await this.$store.dispatch('help/getHelp', {
        userIdNe: this.user.user.id,
        limit: 10,
        statusId: 1,
        cityId: this.user.user.addresses[0].city.id,
      });
    },
  },
};
</script>
<style lang="scss" scoped>
.home {
  background-color: white;
  height: 100%;
  display: flex;
  flex-flow: column;
  justify-content: space-between;
}
</style>
