<template>
  <div>
    <v-avatar :width="size" :height="size">
      <v-img
        center :src="src"
      >
        <template v-slot:placeholder>
          <v-row
            class="fill-height ma-0"
            align="center"
            justify="center"
          >
            <v-progress-circular indeterminate color="danger"></v-progress-circular>
          </v-row>
        </template>
      </v-img>
    </v-avatar>
  </div>
</template>
<script>
export default {
  name: 'Default',
  props: {
    src: { type: String, required: true },
    size: { type: Number, default: 46, required: false },
  },
};
</script>
<style lang="scss" scoped>
.v-avatar {
  min-width: 46px !important;
  display: inherit;
}
</style>
