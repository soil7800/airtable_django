<template>
  <div id="app">
    <router-view/>
  </div>
</template>
<script>
  export default {
    components: {}
}
</script>
<style>
  * {
    box-sizing: border-box;
  }
  body {
    margin: 0;
  }
  #app {
    width: 100%;
    max-width: 800px;
    margin: auto;
    padding: 1rem;
  }
  .btn {
    padding: 0.5rem 2rem;
    border-radius: 0.5rem;
    text-decoration: none;
    font-size: 2rem;
    color: #fff;
    background: #197742;
  }
</style>
