<template>
  <v-container fluid fill-height>
    <v-card width="400" class="mx-auto mt-5">
      <v-toolbar flat>
        <v-toolbar-title>CornerStone Login</v-toolbar-title>
      </v-toolbar>
      <v-card-text>
        <v-form @submit.prevent="onSubmit" id="login-form">
          <v-text-field
            label="Username"
            prepend-icon="mdi-account-circle"
            v-model="username"
          />
          <v-text-field
            :type="showPassword ? 'text' : 'password'"
            label="Password"
            prepend-icon="mdi-lock"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="showPassword = !showPassword"
            v-model="password"
          />
        </v-form>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-btn @click="$router.go(-1)">Cancel</v-btn>
        <v-spacer></v-spacer>
        <v-btn color="info" type="submit" form="login-form">
          Login
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import { LOGIN } from '../store/actions.type';
export default {
  name: 'Login',
  data: () => ({
    username: null,
    password: null,
    showPassword: false,
  }),
  methods: {
    onSubmit() {
      this.$store
        .dispatch(LOGIN, {
          username: this.username,
          password: this.password,
        })
        .then(() => this.$router.back());
    },
  },
  computed: {},
};
</script>

<style></style>
