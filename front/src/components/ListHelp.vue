<template>
  <v-container class="text-center">
    <div v-if="help.helpList && help.helpList.length === 0">
      <p class="display-1 font-weight-medium danger--text">Sem Pedidos</p>
    </div>
    <div v-else>
      <p class="title font-weight-medium primary--text text-left">Pedidos recentes</p>
      <div v-if="help.helpList">
        <Carousel
          :loop="true"
          :scrollPerPage="true"
          :paginationEnabled="false"
          :perPageCustom="[[320, 1], [600, 2], [768, 3]]"
          :paginationActiveColor="'#532594'"
          :spacePadding="20"
          :spacePaddingMaxOffsetFactor="1"
          >
          <Slide  v-for="(help) in help.helpList" :key="help.id_user">
            <HelpCard
              :avatar="help.request_user.avatar"
              :id="help.id"
              :name="help.request_user.first_name"
              :age="$filters.calcAge(help.request_user.birth_date)"
              :createdat="$filters.formatDate(help.created)"
              :description="help.category.description"
              :timeago="$filters.calcTimeCard(help.created)"
            />
          </Slide>
        </Carousel>
        <v-btn to="/requested-helps" text color="primary">Ver todos</v-btn>
      </div>
    </div>

    <p
      v-if="help.helpListError"
      class="block text-center mt-4 red--text">{{help.helpListError}}</p>
    <v-btn
      v-if="help.helpLoading"
      text block x-large
      :loading="true" color="danger"></v-btn>
  </v-container>
</template>
<script>
import { mapState } from 'vuex';
import HelpCard from '@/components/HelpCard.vue';
import { Carousel, Slide } from 'vue-carousel';

export default {
  components: {
    HelpCard,
    Carousel,
    Slide,
  },
  computed: mapState(['help', 'user']),
  data() {
    return {
      newHelp: false,
    };
  },
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
  created() {
    this.listHelp();
  },
};
</script>
<style lang="scss" scoped>
.VueCarousel {
  // max-width: 700px;
  margin: 0 auto;
  &-slide {
    margin: 10px 0px;
  }
}
</style>
