<template>
  <div class="movie-list">
    <MovieResult />
    <MovieSearch />
    <MovieSuggest />
  </div>
</template>

<script>
import "@/assets/css/views/movies.scss"
import MovieResult from "@/components/Movies/MovieResult.vue"
import MovieSearch from "@/components/Movies/MovieSearch.vue"
import MovieSuggest from "@/components/Movies/MovieSuggest.vue"

export default {
  name: "MovieList",
  components: {
    MovieResult,
    MovieSearch,
    MovieSuggest
  }
}
</script>