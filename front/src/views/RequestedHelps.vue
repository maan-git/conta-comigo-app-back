<template>
  <div>
    <HelpRequests :ne="true"/>
  </div>
</template>
<script>
import HelpRequests from '@/components/HelpRequests.vue';

export default {
  components: { HelpRequests },
};
</script>
