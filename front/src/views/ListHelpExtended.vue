<template>
  <v-card>
    <v-tabs
      v-model="tab"
      background-color="primary"
      centered
      dark
    >
      <v-tab
        v-for="item in items"
        :key="item.tab"
      >
        {{ item.tab }}
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item
        v-for="item in items"
        :key="item.tab"
      >
        <v-tab-item
          v-for="content in item.contents"
          :key="content.text">
          <v-card flat>
            <v-card-text>{{ content.text }} <ListItensCard /></v-card-text>
          </v-card>
        </v-tab-item>
      </v-tab-item>
    </v-tabs-items>
  </v-card>
</template>
<script>
import ListItensCard from '@/components/ListItensCard.vue';

export default {
  name: 'ListHelpExtended',
  components: {
    ListItensCard,
  },
  data: () => ({
    tab: null,
    items: [
      {
        tab: 'teste 1',
        contents: [{ text: 'teste content' }, { text: 'teste content 3' }, { text: 'teste content 4' }],
      },
      {
        tab: 'teste 2',
        contents: [{ text: 'teste content' }],
      },
    ],
  }),
};
</script>
