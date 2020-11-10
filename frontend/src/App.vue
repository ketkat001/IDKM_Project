<template>
  <v-app>
    <Navbar></Navbar>
    <router-view></router-view>
    <Footer></Footer>
  </v-app>
</template>

<script>
import "@/assets/css/app.scss"
import Navbar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"


export default {
  name: 'App',

  components: {
    Navbar,
    Footer,
  },

  data: () => ({
    // adaptive navbar needed for scroll aciton
  }),
};
</script>
