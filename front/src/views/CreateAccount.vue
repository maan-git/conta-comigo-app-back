<template>
  <div>
    <CardContainer>
      <div class="text-center">
        <p class="primary--text font-weight-bold title">Cadastro</p>
        <span class="subtitle-1 grey--text">{{text}}</span>
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
