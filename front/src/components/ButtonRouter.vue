<template>
    <div>
        <v-btn
            class="mt-5"
            rounded
            :to=url
            color="primary"
            x-large
        >
            {{text}}
            <v-icon>{{heart}}</v-icon>
        </v-btn>
    </div>
</template>

<script>
export default {
  name: 'ButtonRouter',
  props: ['url', 'text', 'heart'],
};
</script>
