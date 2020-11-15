<template>
  <div class="movie-card">
    <img src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg">
    <div class="movie-content">
      <h2> {{ card.title }} </h2>
      <div class="card-btn">
        <v-col sm="4">
          <v-btn class="info-btn">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
        </v-col>
        <v-col sm="4">
          <v-btn class="info-btn">
            <v-icon>mdi-thumb-up</v-icon>
          </v-btn>
        </v-col>
        <v-col sm="4">
          <v-btn class="info-btn">
            <v-icon>mdi-bookmark</v-icon>
          </v-btn>
        </v-col>
      </div>
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
    }
  }
}
</script>