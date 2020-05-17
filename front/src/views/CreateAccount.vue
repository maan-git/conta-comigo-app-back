<template>
  <div>
    <CardContainer backTo>
      <div class="text-center mb-5">
        <p class="primary--text font-weight-medium headline">Cadastro</p>
        <span class="subtitle-1 txt-color">{{text}}</span>
      </div>
      <UserForm :editavel="editavel"></UserForm>
    </CardContainer>
  </div>
</template>
<script>
import UserForm from '@/components/UserForm.vue';
import CardContainer from '@/components/CardContainer.vue';

export default {
  components: {
    UserForm,
    CardContainer,
  },
  data() {
    return {
      editavel: false,
      // eslint-disable-next-line quotes
      text: `Precisamos de algumas informações para que possamos te ajudar ou fazer de você um voluntário Conta comigo!`,
    };
  },
};
</script>

<style lang="scss" scoped>
.txt-color {
  color: #5f5f5f;
}
</style>style
