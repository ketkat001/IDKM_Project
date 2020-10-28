<template>
  <div class="signup-page">
    This is signup.vue
  </div>
</template>

<script>
export default {
  name: 'Signup',
  data() {
    return {
      emailRE: /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    }
  }

}
</script>
