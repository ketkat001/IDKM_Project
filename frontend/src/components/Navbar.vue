<template>
  <div id="nav">
    <div class="logo">
      <a href="/">
        <img src="@/assets/logo.png" alt="logo">  
      </a>
    </div>
    <div class="nav-list">
      <router-link :to="{ name: 'Home' }">Home</router-link>
      <router-link :to="{ name: 'MovieList' }">MovieList</router-link>
      <router-link :to="{ name: 'Login' }">Login</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style>
</style>