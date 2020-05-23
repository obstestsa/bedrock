<template>
  <v-breadcrumbs :items="breadCrumbs">
    <template v-slot:item="{ item }">
      <v-breadcrumbs-item>
        {{ item.toUpperCase() }}
      </v-breadcrumbs-item>
    </template>
  </v-breadcrumbs>
</template>

<script>
export default {
  props: {
    breadCrumbs: {
      type: Array,
      mandatory: true,
    },
  },
};
</script>

<style></style>
