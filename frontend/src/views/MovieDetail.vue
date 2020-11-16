<template>
  <div class="movie-info">
    <MovieDetailHeader :movie="movie"/>
    <MovieDetailMain :movie="movie"/>
    <MovieDetailFooter/>
  </div>
</template>

<script>
import "@/assets/css/views/movieDetail.scss";
import MovieDetailHeader from "@/components/MovieDetail/MovieDetailHeader.vue"
import MovieDetailMain from "@/components/MovieDetail/MovieDetailMain.vue"
import MovieDetailFooter from "@/components/MovieDetail/MovieDetailFooter.vue"
import axios from "axios";
import SERVER from "@/api/drf.js"

export default {
  name: "MovieDetail",
  components: {
    MovieDetailHeader,
    MovieDetailMain,
    MovieDetailFooter
  },
  mounted() {
    let movieId = this.$route.params.id;
    console.log(SERVER.URL + SERVER.R.MOVIES.movie + movieId + '/')
    axios.get(SERVER.URL + SERVER.R.MOVIES.movie + movieId + '/')
    .then((res) => {
      this.movie = res.data;
    });
  },
  data() {
    return {
      movie: {},
    }
  }
}
</script>