<template>
  <section class="movie-header">
    <div class="movie-poster-wrap">
      <div class="movie-poster">
      </div>
      <div class="content-wrap">
        <div class="movie-info-content">
          <div class="movie-info-content-wrap">
            <div class="movie-info-item-data">
              <span class="movie-year">2020</span>
              <span class="movie-title">몰라</span>
              <span class="movie-genre">
                <a href="">액션</a>
                <a href="">드라마</a>
                <a href="">힐링</a>
                <a href="">망함</a>
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
  name: "MovieDetailHeader"
}
</script>
