<template>
  <div id="app">
    <div id="nav">
      <router-link to="/login" v-if="!login">Login</router-link>
      <router-link to="/profile" v-if="login">Profile</router-link>
      <router-link to="/register" v-if="!login">Register</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  name: "app",
  data() {
    return {
      login: false
    };
  },
  created() {
    const token = localStorage.getItem("token");
    this.login = token !== null;
    if (this.login) {
      this.$router.push({ name: "profile" });
    } else {
      this.$router.push({ name: "login" });
    }
  }
});
</script>


<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
