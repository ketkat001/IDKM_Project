<template>
  <div class="movie-info">
    <MovieDetailHeader/>
    <MovieDetailMain/>
    <MovieDetailFooter/>
  </div>
</template>

<script>
import "@/assets/css/views/movieDetail.scss";
import MovieDetailHeader from "@/components/MovieDetail/MovieDetailHeader.vue"
import MovieDetailMain from "@/components/MovieDetail/MovieDetailMain.vue"
import MovieDetailFooter from "@/components/MovieDetail/MovieDetailFooter.vue"

export default {
  name: "MovieDetail",
  components: {
    MovieDetailHeader,
    MovieDetailMain,
    MovieDetailFooter
  }
}
</script>