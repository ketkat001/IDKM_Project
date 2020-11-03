<template>
  <div class="movie-card" @mouseover="movieHover = true" @mouseout="movieHover = false">
    <img src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg">
    <div class="movie-content" v-if="movieHover">
      <h2> {{ card.title }} </h2>
      <v-row>
        <v-col cols="12" sm="3">
          <v-btn>
            <v-icon>mdi-heart</v-icon>
          </v-btn>
        </v-col>
      </v-row>
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