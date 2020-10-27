<template>
  <div id="app">
    <div id="nav">
      <router-link :to="{ name: 'Home' }">Home</router-link> 
      <router-link :to="{ name: 'Login' }">Login</router-link> 
      <router-link :to="{ name: 'MovieList' }">MovieList</router-link> 
    </div>
    <router-view/>
  </div>
</template>

<script>
import "@/assets/css/app.scss"

export default {}
</script>
