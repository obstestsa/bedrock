<template>
  <v-app>
    <AppLayout v-if="!layout" />
    <SimpleLayout v-else />
    <SnackBar />
  </v-app>
</template>

<script>
import AppLayout from '@/components/AppLayout';
import SimpleLayout from '@/components/SimpleLayout';
import SnackBar from '@/components/SnackBar';
import ThemeService from '@/services/theme.service';
export default {
  name: 'App',
  computed: {
    layout() {
      return this.$route.meta.plainLayout;
    },
  },
  components: {
    AppLayout,
    SimpleLayout,
    SnackBar,
  },
  mounted() {
    if (ThemeService.getDarkTheme() === 'true') {
      this.$vuetify.theme.dark = true;
    } else {
      this.$vuetify.theme.dark = false;
    }
  },
  data: () => ({}),
};
</script>
