<template>
  <div class="movie-search">
    <MovieSearchBox />
  </div>
</template>

<script>
import "@/assets/css/components/movies/movieSearch.scss"
import MovieSearchBox from "@/components/Movies/MovieSearchBox.vue"

export default {
  name: "MovieSearch",
  components: {
    MovieSearchBox
  }
  

}
</script>