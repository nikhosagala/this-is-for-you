<template>
  <div class="about">
    <h1>This is a register page 2</h1>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';

@Component
export default class RegisterComponent extends Vue {
  @Prop() private msg!: string;
}
</script>

