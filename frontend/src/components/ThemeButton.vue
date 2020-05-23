<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ on }">
      <v-btn icon @click="toggleTheme" v-on="on">
        <v-icon v-if="dark" dark>mdi-weather-night</v-icon>
        <v-icon v-else dark color="orange">mdi-weather-sunny</v-icon>
      </v-btn>
    </template>
    <span>Dark Theme</span>
  </v-tooltip>
</template>

<script>
import ThemeService from '@/services/theme.service';
export default {
  name: 'ThemeButton',
  data: () => ({
    dark: ThemeService.getDarkTheme() === 'true',
  }),
  methods: {
    toggleTheme() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
      this.dark = !this.dark;
      ThemeService.setDarkTheme(this.$vuetify.theme.dark);
    },
  },
};
</script>

<style></style>
