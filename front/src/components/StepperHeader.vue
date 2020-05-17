<template>
  <div class="stepper-head">
    <div class="stepper-head__line"></div>
    <div v-for="(step, i) in steps" :key="i"
      class="stepper-head__step"
      :class="{'current-step': ( i + 1 === currenctStep) || i < currenctStep }"
      @click="gotoStep(i + 1)"
    >
      <div class="step__number">
        {{i + 1}}
      </div>
      <span class="step__label">
        {{step.label}}
      </span>
    </div>
  </div>
</template>
<script>
export default {
  props: ['currenctStep', 'steps'],
  methods: {
    gotoStep(step) {
      this.$store.dispatch('register/setStep', step);
    },
  },
};
</script>
<style lang="scss" scoped>
.stepper-head{
  position: relative;
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding: 0 3%;
  &__step {
    z-index: 10;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
    .step {
      &__number {
        $sizes: 30px;
        width: $sizes;
        height: $sizes;
        line-height: 29px;
        color: #bfbfbf;
        border: solid 2px #bfbfbf;
        background-color: #ededed;
        font-size: 18px;
        font-weight: 500;
        border-radius: 100%;
        text-align: center;
      }
      &__label {
        margin-top: 10px;
        font-size: 14px;
        color: #bfbfbf;
        max-width: 60px;
        line-height: 16px;
        text-align: center;
      }
    }
    &.current-step {
      .step{
        &__number {
          background-color: #532594;
          border-color: #532594;
          color: white;
        }
        &__label {
          color: #5f5f5f;
        }
      }
    }
  }
  &__line {
    width: 83%;
    height: 2px;
    border: solid 1px #bfbfbf;
    position: absolute;
    z-index: 0;
    top:14px;
    transform: translateX(-50%);
    left: 50%;
  }
}
</style>
