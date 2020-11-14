<template>
  <section class="movie-main-content">
    <div class="content-wrap">
      <div class="movie-overview">
        <h2>줄거리</h2>
        <p>{{ movie.overview }}</p>
      </div>
      <div class="side-main">
        <div class="movie-side-poster">
          <img :src="'//image.tmdb.org/t/p/original/' + movie.poster_url" width="272" height="408" class="real">
        </div>
      </div>
      <div class="movie-actors">
        <h2>주요 출연진</h2>
        <div class="actor-list row">
          <ActorCard class="actor-card" v-for="actor in movie.actors" :key="actor.id" :actor="actor"/>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import "@/assets/css/components/movieDetail/movieDetailMain.scss";
import ActorCard from "@/components/MovieDetail/ActorCard.vue";



export default {
  name: "MovieDetailMain",
  components: {
    ActorCard,
  },
  props: ['movie'],
}
</script>
