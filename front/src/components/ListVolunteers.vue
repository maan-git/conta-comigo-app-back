<template>
  <v-container class="list-volunteers text-center">

    <p v-if="user.users && user.users.length === 0"
      class="display-1 font-weight-medium danger--text">Sem Voluntarios</p>
    <p v-else
      class="title font-weight-medium primary--text text-left">Voluntarios</p>
    <div v-if="user.users">
      <Carousel
        :loop="true"
        :scrollPerPage="true"
        :paginationEnabled="false"
        :perPageCustom="[[320, 3], [600, 6], [800, 8]]"
        :paginationActiveColor="'#532594'"
        :spacePadding="20"
        :spacePaddingMaxOffsetFactor="1"
      >
        <Slide v-for="(user, i) in user.users" :key="i">
          <div class="volunteer" @click="volunteerDetails(user.id)">
            <DefaultAvatar :src="user.avatar" :size="60" />
            <span>{{user.first_name}}</span>
          </div>
        </Slide>
      </Carousel>
      <ButtonRouter
        url='/create-help'
        text='Preciso de ajuda!'
        heart=$heart>
      </ButtonRouter>
    </div>
    <v-btn
      v-if="user.usersLoginLoading"
      text block x-large
      :loading="true" color="primary"></v-btn>
  </v-container>
</template>
<script>
import { mapState } from 'vuex';
import { Carousel, Slide } from 'vue-carousel';
import ButtonRouter from '@/components/ButtonRouter.vue';
import DefaultAvatar from '@/components/DefaultAvatar.vue';


export default {
  components: {
    Carousel,
    Slide,
    ButtonRouter,
    DefaultAvatar,
  },
  computed: mapState(['user']),
  methods: {
    volunteerDetails(id) {
      this.$router.push(`/volunteer-details?userId=${id}`);
    },
  },
  created() {
    this.$store.dispatch('user/getUsers',
      `limit=10&ordering=-date_joined&id__ne=${this.user.user.id}&city_id=${this.user.user.addresses[0].city.id}`);
  },
};
</script>
<style lang="scss" scoped>
.volunteer {
  width: 80px;
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  span {
    margin-top: 15px;
    font-size: 14px;
    color: #5f5f5f;
    transition: all .5s ease-in-out;
  }
  &:hover {
    span {
      color: #532594;
    }
  }
}
</style>
