<template>
  <div class="request-helps">
    <CardContainer :title="title" backTo>
      <div class="request-button my-3">
        <v-btn color="primary"
        :outlined="hidden"
        :text="!hidden"
        x-large
        rounded
        @click="listHelp()"><b>Aguardando<br/>voluntários</b></v-btn>
        <v-btn color="primary"
        :outlined="!hidden"
        :text="hidden"
        x-large
        rounded
        @click="listApproved()"><b>Aceitos</b></v-btn>
      </div>
      <div class="request-helps-content" v-if="help && help.helpList && help.helpList.length">
        <v-row v-if="hidden" class="row-list">
          <v-col
            cols="12"
            :sm="smSize()"
            xs="12" v-for="(help) in help.helpList"
            :key="help.id_user"
          >
            <HelpCard
              :avatar="help.request_user.avatar"
              :id="help.id"
              :name="help.request_user.first_name"
              :age="$filters.calcAge(help.request_user.birth_date)"
              :createdat="$filters.formatDate(help.created)"
              :description="help.category.description"
              :block="true"
              :templateAccount="false"
              :btnDisable="btnDisable"
              :timeago="$filters.calcTimeCard(help.created)"
              :label="btnLabel"
            />
          </v-col>
        </v-row>
        <v-row v-else class="row-list">
          <v-col
            cols="12"
            :sm="smSize()"
            xs="12"
            v-for="(help) in help.helpList" :key="help.id_user"
          >
            <HelpCard
              v-if="help.helping_users[0]"
              :avatar="help.request_user.avatar"
              :id="help.id"
              :name="help.request_user.first_name"
              :age="$filters.calcAge(help.request_user.birth_date)"
              :createdat="$filters.formatDate(help.created)"
              :description="help.category.description"
              :timeago="$filters.calcTimeCard(help.created)"
              :block="true"
              :templateAccount="true"
              :nameAssociate="help.helping_users[0].helper_user.first_name"
              :stateAssociate="help.helping_users[0].status.description"
              :imageAssociate="help.helping_users[0].helper_user.avatar"
              :label="btnLabel"
            />
          </v-col>
        </v-row>
        <div class="text-center" v-if="help.helpListCount > limit">
          <v-pagination
            v-on:next="next"
            v-on:previous="previous"
            v-on:input="paginationInput"
            v-model="page"
            :length="pagesLength()"
            circle
          ></v-pagination>
        </div>
      </div>
      <div class="request-helps-content" v-else-if="!help.helpLoading">
        <p class="title danger--text text-center pa-5">Sem pedidos disponíveis</p>
      </div>
      <div v-else>
        <p class="title danger--text text-center pa-5">Carregando</p>
        <v-btn loading color="danger" text large block></v-btn>
      </div>
    </CardContainer>
  </div>
</template>
<script>
import { mapState } from 'vuex';
import HelpCard from '@/components/HelpCard.vue';
import CardContainer from '@/components/CardContainer.vue';

export default {
  components: { CardContainer, HelpCard },
  computed: mapState(['help', 'user']),
  props: {
    ne: { type: Boolean },
    btnDisable: { type: Boolean, default: false },
  },
  data() {
    return {
      hidden: false,
      dataListHelp: null,
      dataListApproved: null,
      title: 'Pedidos',
      btnLabel: null,
      page: 1,
      offset: 0,
      limit: 6,
    };
  },
  methods: {
    smSize() {
      return (this.help.helpList && this.help.helpList.length > 2) ? 6 : 12;
    },
    pagesLength() {
      const plus = (this.help.helpListCount / this.limit) % 2 === 0 ? 0 : 1;
      // eslint-disable-next-line radix
      const ret = parseInt((this.help.helpListCount / this.limit) + plus);
      return ret;
    },
    listHelp() {
      if (this.hidden) return;
      this.$store.dispatch('help/clearHelpState');
      this.page = 1;
      this.offset = 0;
      this.getListHelp();
    },
    async getListHelp() {
      this.dataListHelp = null;
      this.dataListHelp = {
        limit: this.limit,
        offset: this.offset,
        statusId: 1, // Criado
        cityId: this.user.user.addresses[0].city.id,
      };
      if (this.ne) this.dataListHelp.userIdNe = this.user.user.id;
      else this.dataListHelp.userId = this.user.user.id;
      await this.$store.dispatch('help/getHelp', this.dataListHelp);
      this.hidden = true;
    },
    listApproved() {
      if (!this.hidden) return;
      this.$store.dispatch('help/clearHelpState');
      this.page = 1;
      this.offset = 0;
      this.getListApproved();
    },
    async getListApproved() {
      this.dataListApproved = null;
      this.dataListApproved = {
        limit: this.limit,
        offset: this.offset,
        statusId: 20, // Em andamento
      };
      if (this.ne) {
        this.dataListApproved.userIdNe = this.user.user.id;
        this.dataListApproved.cityId = this.user.user.addresses[0].city.id;
      } else this.dataListApproved.userId = this.user.user.id;
      await this.$store.dispatch('help/getHelp', this.dataListApproved);
      this.hidden = false;
    },
    paginationInput(e) {
      this.offset = this.limit * (e - 1);
      this.onlyGo();
    },
    next() {
      this.offset += this.limit;
      this.onlyGo();
    },
    previous() {
      this.offset -= this.limit;
      this.onlyGo();
    },
    onlyGo() {
      if (this.hidden) this.getListHelp();
      else this.getListApproved();
    },
  },
  created() {
    this.listHelp();
    if (this.$router.currentRoute.name === 'RequestedHelpsUser') {
      this.title = 'Meus Pedidos';
      this.btnLabel = 'Mais Info';
    }
  },
  beforeDestroy() {
    this.$store.dispatch('help/clearHelpState');
  },
};
</script>
<style lang="scss" scoped>
.request-helps{
  height: 100%;
  &-content {
    min-width: 400px;
    min-height: 500px;
    @media screen and ( max-width: 600px) { min-width: 100%; }
  }
}
.request-button{
  width: 100%;
  display: flex;
  justify-content: space-around;
}
.row-list{
  min-height: 500px;
}
</style>
