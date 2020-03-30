<template>
  <div class="card-container" :class="{'justify-space-between': $vuetify.breakpoint.xs}">
    <div class="card-container__img text-center my-5">
      <img width="178" :src="require('../assets/logo_completa.svg')">
    </div>
    <div class="card-container__card">
      <slot></slot>
    </div>
  </div>
</template>
<script>
export default {
  name: 'CardContainer',
};
</script>
<style lang="scss" scoped>
  .card-container {
    width:100%;
    height:100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    &__card {
      background-color: white;
      border-radius: 54px;
      padding: 20px;
      max-width: 800px;
      margin-bottom: 100px;
    }
    @media screen and ( max-width: 600px) {
      .card-container {
        &__img {
          height: 100%;
          display: flex;
        }
        &__card {
          align-self: stretch;
          border-bottom-left-radius: 0;
          border-bottom-right-radius: 0;
          margin-bottom: 0;
        }
      }
    }
  }
</style>
