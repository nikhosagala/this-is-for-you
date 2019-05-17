<template>
  <div>
    {{email}}
    <div>
      <button type="submit" class="btn btn-default" @click="logout">Logout</button>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { authService } from "../services/auth.service";
import { Component, Prop, Watch } from "vue-property-decorator";

@Component
export default class Register extends Vue {
  email: string = "";
  errors: string[] = [];

  created() {
    this.getProfile();
  }

  public logout() {
    authService.removeToken();
    this.$router.push({ name: "login" });
  }

  public getProfile() {
    authService
      .getProfile()
      .then((res) => {
        this.email = res.data;
      })
      .catch((error) => {
        this.errors.push(error.response.data);
      });
  }
}
</script>
