<template>
  <div class="help-card" :class="{'help-card--bloq': block}">
    <div class="help-card--header">
      <DefaultAvatar :src="avatar"/>
      <div class="help-card--header__text">
        <p>
          {{createdat}}<br>{{timeago}}
        </p>
      </div>
    </div>
    <div class="help-card--content">
      <p class="help-card--content__title">{{name}}, {{age}} anos</p>
      <p class="help-card--content__text">{{mydescription}}</p>
    </div>
    <div v-if="!templateAccount" class="help-card--footer">
      <v-btn
        :to="getUrl()"
        block
        rounded
        color="primary"
        :disabled="btnDisable">
        {{label? label: 'Conta Comigo'}}
        <v-icon right dark>$heart</v-icon>
      </v-btn>
    </div>
    <div v-else class="help-card--footer account">
      <div class="content secondary--text">
        <p class="subtitle-2 mb-0">{{nameAssociate}}</p>
        <p class="caption mb-0">{{stateAssociate}}</p>
      </div>
      <div class="image">
        <DefaultAvatar :size="34" :src="imageAssociate"/>
      </div>
    </div>
  </div>
</template>
<script>
import DefaultAvatar from '@/components/DefaultAvatar.vue';

export default {
  props: ['id', 'description',
    'name', 'age', 'createdat', 'timeago', 'user_request', 'avatar', 'block',
    'templateAccount', 'nameAssociate', 'stateAssociate', 'imageAssociate',
    'btnDisable', 'label'],
  components: { DefaultAvatar },
  data() {
    return {
      mydescription: '',
      myimg: '../assets/icone.svg',
    };
  },
  methods: {
    getUrl() {
      return `/help-details?id=${this.id}`;
    },
  },
  created() {
    if (this.description.length > 120) {
      this.mydescription = `${this.description.substr(0, 120)}...`;
    } else {
      this.mydescription = this.description;
    }
  },
};
</script>
<style lang="scss" scoped>
.help-card {
  max-width: 200px;
  min-height: 216px;
  // height: 100%;
  border-radius: 10px;
  padding: 12px;
  box-shadow: 0px 0px 3px 0 rgba(0, 0, 0, 0.16);
  $quadsize: 46px;
  $txtcolor: #5f5f5f;
  display: flex;
  flex-flow: column;
  justify-content: space-between;
  // margin: 10px 30px;

  &--header {
    display: flex;
    align-content: center;
    justify-content: space-between;
    margin-bottom: 10px;
    &__text{
      color: $txtcolor;
      font-size: 12px;
      text-align: right;
      font-weight: 500;
      p {
        margin-bottom: 0;
      }
    }
  }
  &--content {
    color: $txtcolor;
    font-size: 12px;
    text-align: left;
    &__title {
      font-size: 16px;
      font-weight: 500;
    }
  }
  &--bloq{
    max-width: 100%;
  }
}
.account {
  width: 100%;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  .content {
    display: inline-block;
    text-align: right;
  }
  .image {
    display: inline-block;
  }
}
</style>
