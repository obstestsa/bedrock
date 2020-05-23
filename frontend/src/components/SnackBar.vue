<template>
  <v-snackbar v-model="show" :color="color" :timeout="timeout">
    {{ message }}
    <v-btn small @click="close">Close</v-btn>
  </v-snackbar>
</template>

<script>
import { SET_SNACKBAR } from '../store/mutations.type';
export default {
  data: () => ({
    show: false,
    message: '',
    color: '',
    timeout: 10000,
  }),
  created() {
    this.$store.subscribe((mutation, state) => {
      if (mutation.type === SET_SNACKBAR) {
        this.message = state.snackBar.message;
        this.color = state.snackBar.color;
        this.show = true;
      }
    });
  },
  methods: {
    close() {
      this.show = false;
    },
  },
};
</script>

<style></style>
