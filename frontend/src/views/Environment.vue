<template>
  <h1>Environment Page</h1>
</template>

<script>
export default {
  name: 'Environment',
  data: () => ({
    breadCrumbs: ['Home', 'Sor', 'Environment'],
    loadingText: 'Loading Environments, Please wait.',
    search: '',
    headers: [
      {
        text: 'Name',
        align: 'start',
        value: 'name',
      },
    ],
  }),
};
</script>

<style></style>
