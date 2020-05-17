<template>
  <div v-if="user.volunteerDetails">
    <CardContainer :hideLogo="true">
      <div class="text-center">
        <p class="primary--text font-weight-bold title">
          {{user.volunteerDetails.first_name}},
          {{$filters.calcAge(user.volunteerDetails.birth_date)}} anos</p>
      </div>

      <v-flex class="how-to">
        <v-img width="350" class="img-center"
          center :src="user.volunteerDetails.avatar"></v-img>
        <div class="text-center margin-text">
          <p class="subtitle-1 grey--text"
          >Cadastrou-se em {{$filters.formatDate(user.volunteerDetails.date_joined)}}</p>
          <p class="subtitle-1 grey--text"
          >Grupo de risco: {{$filters.isRiskGroup(user.volunteerDetails.is_at_risk_group)}}</p>
        </div>
      </v-flex>
    <p v-if="user.volunteerDetailsError"
       class="block text-center mt-4 red--text">{{user.volunteerDetailsError}}</p>
    </CardContainer>
  </div>
</template>
<script>

import { mapState } from 'vuex';
import CardContainer from '@/components/CardContainer.vue';

export default {
  components: {
    CardContainer,
  },
  computed: mapState(['user']),
  created() {
    this.$store.dispatch('user/getVolunteerDetails', this.$route.query.userId);
  },
};
</script>

<style lang="scss">
.margin-text{
  margin:12% 0;
}
.img-center{
  margin:0 auto;
}
</style>
