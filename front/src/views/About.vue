<template>
  <div class="about">
    <h1>This is an about page</h1>
    <p>{{user.list}}</p>
  </div>

</template>
<script>

import { mapState } from 'vuex';

export default {
  computed: mapState(['user']),
};
</script>
