<template>
  <div id="nav">
    <div class="logo">
      <p>
        <a href="/">
          <!-- <img src="@/assets/logo.png" alt="logo"/> -->
        </a>
      </p>
    </div>
    <div class="nav-list">
      <router-link :to="{ name: 'Home' }">Home</router-link>
      <router-link :to="{ name: 'MovieList' }">MovieList</router-link>
      <router-link :to="{ name: 'Login' }">Login</router-link>
    </div>
  </div>
</template>

<script>
import "@/assets/css/components/navbar.scss";

export default {
  name: "Navbar",
};
</script>
