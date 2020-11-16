<template>
  <div id="nav" :class="{ 'navbar--hidden': !showNavbar }">
    <div class="logo">
      <a href="/">
        <img class="logo-img" src="@/../public/logo.png" alt="logo" />
      </a>
    </div>
    <div class="nav-list">
      <router-link :to="{ name: 'Home' }">Home</router-link>
      <router-link :to="{ name: 'Movies' }">Movies</router-link>
      <router-link v-show="!isLogin" :to="{ name: 'Login' }">Login</router-link>
      <a v-show="isLogin" @click="logout()">Logout</a>
    </div>
  </div>
</template>

<script>
import "@/assets/css/components/navbar.scss";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Navbar",
  mounted() {
    this.lastScrollPosition = window.pageYOffset;
    window.addEventListener("scroll", this.onScroll);
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.onScroll);
  },
  computed: {
    ...mapGetters("accounts", ["isLogin"]),
  },
  methods: {
    ...mapActions("accounts", ["logout"]),
    onScroll() {
      let currentScrollPosition =
        window.pageYOffset || document.documentElement.scrollTop;
      if (currentScrollPosition < 0) {
        return;
      }
      if (Math.abs(currentScrollPosition - this.lastScrollPosition) < 60) {
        return;
      }
      this.showNavbar = currentScrollPosition < this.lastScrollPosition;
      this.lastScrollPosition = currentScrollPosition;
    },
  },
  data() {
    return {
      showNavbar: true,
    };
  },
};
</script>
