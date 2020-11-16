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
                <a href="" v-for="genre in (movie.genres)" :key="genre.id">{{ genre['genre'] }}</a>
              </span>
            </div>
            <div class="movie-buttons">
              <v-btn icon>
                <font-awesome-icon :icon="['fab', 'youtube']"/>
              </v-btn>
              <v-btn icon @click="changeHeartIcon">
                <v-icon v-show="heartIcon" color="pink">mdi-heart</v-icon>
                <v-icon v-show="!heartIcon">mdi-heart</v-icon>
              </v-btn>
              <v-btn icon @click="changeBookmarkIcon">
                <v-icon v-show="bookmarkIcon" color="green">mdi-bookmark</v-icon>
                <v-icon v-show="!bookmarkIcon">mdi-bookmark</v-icon>
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
    },
  },
  methods: {
    changeHeartIcon() {
      this.heartIcon = !this.heartIcon
    },
    changeBookmarkIcon() {
      this.bookmarkIcon = !this.bookmarkIcon
    }
  },
  data() {
    return {
      heartIcon: false,
      bookmarkIcon: false,
    }
  }
  
}
</script>