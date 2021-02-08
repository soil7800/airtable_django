<template>
  <div class="not_found">
    <h1>Oops!</h1>
    <h2>404 Not Found</h2>
    <router-link class="btn" :to="{name: 'Home'}">Домой</router-link>
  </div>
</template>
<style scoped>
  .not_found {
    text-align: center;
  }
</style>