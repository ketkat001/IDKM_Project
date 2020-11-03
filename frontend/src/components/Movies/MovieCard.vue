<template>
  <div class="movie-card" @mouseover="movieHover = true" @mouseout="movieHover = false">
    <img src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg">
    <div class="movie-content" v-if="movieHover">
      <h2> {{ card.title }} </h2>
      <h4> {{card.text}} content </h4>
    </div>
  </div>
</template>

<script>
import "@/assets/css/components/movies/movieCard.scss";
export default {
  name: "MoviesCard",
  props: {
    card: {
      type: Object
    },
  },
  data () {
    return {
      movieHover: false
    }
  }
}
</script>