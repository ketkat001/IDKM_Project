<template>
  <div id="nav">
    <p class="nav-list">
      <router-link :to="{ name: 'Home' }">Home</router-link>
      <router-link :to="{ name: 'MovieList' }">MovieList</router-link>
      <router-link :to="{ name: 'Login' }">Login</router-link>
    </p>
  </div>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style>
</style>