<template>
  <div class="movie-list">
    <MovieResult v-show="hasSearch" />
    <MovieSearch />
    <MovieSuggest />
  </div>
</template>

<script>
import "@/assets/css/views/movies.scss";
import MovieResult from "@/components/Movies/MovieResult.vue";
import MovieSearch from "@/components/Movies/MovieSearch.vue";
import MovieSuggest from "@/components/Movies/MovieSuggest.vue";
import { mapState } from "vuex";

export default {
  name: "MovieList",
  components: {
    MovieResult,
    MovieSearch,
    MovieSuggest,
  },
  computed: {
    ...mapState("movies", ["movieList"]),
    hasSearch() {
      return !!this.movieList;
    },
  },
  data() {
    return {
      
    };
  },
};
</script>