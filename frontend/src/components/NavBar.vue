<template>
  <nav>
    <!-- Navigation Bar -->
    <v-app-bar :clipped-left="$vuetify.breakpoint.lgAndUp" app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title style="width: 300px" class="ml-0 pl-4">
        <span class="font-weight-light">Corner</span>
        <span>Stone</span>
      </v-toolbar-title>
      <v-text-field
        flat
        solo-inverted
        hide-details
        prepend-inner-icon="mdi-magnify"
        label="Search"
      />
      <v-spacer />
      <v-btn icon>
        <v-icon>mdi-bell</v-icon>
      </v-btn>
      <ThemeButton />
      <v-menu v-if="isAuthenticated" bottom :offset-y="offset">
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon>mdi-account-circle</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item @click.stop>
            <v-list-item-action>
              <v-icon>mdi-account-settings</v-icon>
            </v-list-item-action>
            <v-list-item-title>Profile</v-list-item-title>
          </v-list-item>
          <v-list-item @click="logout">
            <v-list-item-action>
              <v-icon>mdi-logout</v-icon>
            </v-list-item-action>
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
      <v-tooltip v-else bottom>
        <template v-slot:activator="{ on }">
          <v-btn icon :to="routes.login" v-on="on">
            <v-icon v-if="dark" dark>mdi-weather-night</v-icon>
            <v-icon v-else dark>mdi-login-variant</v-icon>
          </v-btn>
        </template>
        <span>Login</span>
      </v-tooltip>
    </v-app-bar>

    <!-- Navigation Drawer -->
    <v-navigation-drawer
      v-model="drawer"
      :clipped="$vuetify.breakpoint.lgAndUp"
      app
    >
      <v-list flat dense>
        <template v-for="(item, index) in items">
          <v-subheader v-if="item.header" :key="item.header">{{
            item.header
          }}</v-subheader>
          <v-divider v-else-if="item.divider" :key="index"></v-divider>
          <v-list-group
            v-else-if="item.children"
            :key="item.title"
            :prepend-icon="item.icon"
            :to="item.link"
          >
            <template v-slot:activator>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </template>
            <v-list-item v-for="(child, i) in item.children" :key="i">
              <v-list-item-action v-if="child.icon"
                ><v-icon>{{ child.icon }}</v-icon></v-list-item-action
              >
              <v-list-item-content>
                <v-list-item-title>{{ child.title }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
          <v-list-item v-else :key="item.title" :to="item.link">
            <v-list-item-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>

<script>
import { mapGetters } from 'vuex';
import { LOGOUT } from '../store/actions.type';
import ThemeButton from './ThemeButton';
// TODO: Fix active link bug
export default {
  name: 'NavBar',
  components: {
    ThemeButton,
  },
  data: () => ({
    dark: false,
    offset: true,
    drawer: null,
    routes: {
      home: { name: 'home' },
      login: { name: 'login' },
    },
    items: [
      { header: 'Dashboard' },
      {
        icon: 'mdi-view-dashboard',
        title: 'Home',
        link: { name: 'home' },
      },
      { header: 'SOR' },
      { icon: 'mdi-server', title: 'Servers', link: { name: 'server' } },
      {
        icon: 'mdi-hexagon',
        title: 'Environments',
        link: { name: 'environment' },
      },
      {
        icon: 'mdi-hexagon-multiple',
        title: 'Clusters',
        link: { name: 'cluster' },
      },
      {
        icon: 'mdi-laptop',
        title: 'Application',
        link: { name: 'application' },
      },
      {
        icon: 'mdi-microsoft-windows',
        title: 'OS',
        link: { name: 'operating-system' },
      },
      {
        icon: 'mdi-folder',
        title: 'Types',
        children: [
          { icon: 'mdi-domain', title: 'Domains', link: null },
          { icon: 'mdi-layers', title: 'EnvType', link: null },
          {
            icon: 'mdi-star-box-multiple',
            title: 'Owner',
            link: null,
          },
        ],
      },
      { header: 'Monitoring' },
      { icon: 'mdi-contacts', title: 'Contacts', link: null },
      { icon: 'mdi-book-account', title: 'Subscriptions', link: null },
      { icon: 'mdi-bell-off', title: 'Downtime', link: null },
    ],
  }),
  methods: {
    logout() {
      this.$store.dispatch(LOGOUT).then(() => {
        this.$router.go(0);
      });
    },
  },
  computed: {
    ...mapGetters(['isAuthenticated']),
  },
};
</script>

<style></style>
