<template>
  <div>
    <Navigation></Navigation>
  </div>
  <router-view />
</template>

<script>
import Navigation from "@/components/global/Navigation.vue";

export default {
  components: {
    Navigation,
  },
};
</script>
