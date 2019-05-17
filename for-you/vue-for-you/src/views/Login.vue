<template>
  <div>
    <p v-if="errors.length">
      <b>Please correct the following error(s):</b>
    </p>
    <ul>
      <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
    </ul>
    <div class="form-group">
      <div>
        <input v-model="email" type="email" placeholder="Email" required>
      </div>
      <div>
        <input v-model="password" type="password" placeholder="Password" required>
      </div>
    </div>
    <button type="submit" class="btn btn-default" @click="login">Login</button>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { authService } from "../services/auth.service";
import { Component, Prop, Watch } from "vue-property-decorator";

@Component
export default class Register extends Vue {
  email: string = "";
  password: string = "";
  errors: string[] = [];

  created() {
    if (authService.isLoggedIn()) {
      this.$router.push({ name: "profile" });
    }
  }

  public login() {
    authService
      .login(this.email, this.password)
      .then((res) => {
        authService.setToken(res.data.token);
        this.$router.push({ name: "profile" });
      })
      .catch((error) => {
        this.errors.push(error.response.data);
      });
  }
}
</script>
