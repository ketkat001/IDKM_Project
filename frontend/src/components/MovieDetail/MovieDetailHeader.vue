<template>
  <section class="movie-header">
    <div class="movie-poster-wrap">
      <div class="movie-poster" :style="{backgroundImage: 'url('+ this.poster_url + ')'}">
      </div>
      <div class="content-wrap">
        <div class="movie-info-content">
          <div class="movie-info-content-wrap">
            <div class="movie-info-item-data">
              <span class="movie-year">{{ movie.release_date.split('-')[0] }}</span>
              <span class="movie-title">{{ movie.title }}</span>
              <span class="movie-genre">
                <a href="" v-for="genre in (movie.genres.split(','))" :key="genre.id">{{ genre }}</a>
              </span>
            </div>
            <div class="movie-buttons">
              <v-btn icon>
                <span class="iconify" data-icon="mdi-youtube" data-inline="false"></span>
              </v-btn>
              <v-btn icon>
                <v-icon>mdi-heart</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon>mdi-bookmark</v-icon>
              </v-btn>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import "@/assets/css/components/movieDetail/movieDetailHeader.scss";

export default {
  name: "MovieDetailHeader",
  props: {
    movie: Object,
  },
  computed: {
    poster_url() {
      return '//image.tmdb.org/t/p/original/' + this.movie.poster_url
    }
  }
  
}
</script>