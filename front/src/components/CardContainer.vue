<template>
  <div class="conte">
    <v-container class="text-center my-5">
      <img width="178" :src="require('../assets/logo_completa.svg')">
    </v-container>
    <div class="conte-card">
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
  .conte {
    display: flex;
    flex-direction: column;
    position:absolute;
    width:100%;
    height:100%;
    align-items: center;
    justify-content: center;
    &-card {
      background-color: white;
      border-radius: 54px;
      padding: 20px;
      max-width: 800px;
    }
    @media screen and ( max-width: 600px) {
      .conte {
        &-card {
          height: 100%;
          align-self: stretch;
          border-bottom-left-radius: 0;
          border-bottom-right-radius: 0;
        }
      }
    }
  }
</style>
