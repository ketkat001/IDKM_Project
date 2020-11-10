<template>
  <div id="nav" :class="{ 'navbar--hidden': !showNavbar }">
    <div class="logo">
      <p>
        <a href="/">
          <span>LoGo</span>
          <!-- <img src="@/assets/logo.png" alt="logo"/> -->
        </a>
      </p>
    </div>
    <div class="nav-list">
      <router-link :to="{ name: 'Home' }">Home</router-link>
      <router-link :to="{ name: 'Movies' }">Movies</router-link>
      <router-link v-show="!islogin" :to="{ name: 'Login' }">Login</router-link>
      <router-link v-show="islogin" :to="{ name: 'Home' }">Logout</router-link>
    </div>
  </div>
</template>

<script>
import "@/assets/css/components/navbar.scss";
import { mapGetters } from "vuex"

export default {
  name: "Navbar",
  mounted() {
    this.lastScrollPosition = window.pageYOffset
    window.addEventListener('scroll', this.onScroll)
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.onScroll)
  },
  computed: {
    ...mapGetters(["islogin"])
  },
  methods: {
    onScroll() {
      let currentScrollPosition = window.pageYOffset || document.documentElement.scrollTop
      if (currentScrollPosition < 0) {
        return
      }
      if (Math.abs(currentScrollPosition - this.lastScrollPosition) < 60) {
        return
      }
      this.showNavbar = currentScrollPosition < this.lastScrollPosition
      this.lastScrollPosition = currentScrollPosition
    },
  },
  data() {
    return {
      showNavbar: true,
    }
  }
};
</script>
