<template>
  <div>
    <div class="form-group">
      <div>
        <input v-model="email" type="email" placeholder="Email" required>
      </div>
      <div>
        <input v-model="password" type="password" placeholder="Password" required>
      </div>
    </div>
    <button type="submit" class="btn btn-default" @click="register">Register</button>
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

  public register() {
    authService.register(this.email, this.password);
  }
}
</script>
