<template>
  <v-breadcrumbs :items="getBreadCrumbs">
    <template v-slot:item="{ item }">
      <v-breadcrumbs-item>
        {{ item.toUpperCase() }}
      </v-breadcrumbs-item>
    </template>
  </v-breadcrumbs>
</template>

<script>
export default {
  computed: {
    getBreadCrumbs() {
      let breadCrumbs = ['Home'];
      const currentPath = this.$route.path.split('/');
      return breadCrumbs.concat(currentPath.splice(1, currentPath.length));
    },
  },
};
</script>

<style></style>
