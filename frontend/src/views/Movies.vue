<template>
  <div class="movie-list">
    <MovieSearch />
  </div>
</template>

<script>
import "@/assets/css/movieList.scss"
import MovieSearch from "@/components/Movies/MovieSearch.vue"

export default {
  name: "MovieList",
  components: {
    MovieSearch
  }

}
</script>