<template>
  <section class="movie-footer">
    <div class="content-wrap">
      <div class="movie-recommend">
        <h2>이 영화와 비슷한 영화</h2>
        <div class="row">
          <MovieCard class="recommend-card" v-for="card in cardList" :key="card.id" :card="card" />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import "@/assets/css/components/movieDetail/movieDetailFooter.scss";
import MovieCard from "@/components/Movies/MovieCard.vue";

export default {
  name: "MovieDetailFooter",
  components: {
    MovieCard,
  },
  data() {
    return {
      cardList: [
        {
          card1: 1,
          id: 1,
          title: "First Title",        
          text: "first",
        },
        {
          card1: 2,
          id: 2,
          title: "Second Title",
          text: "second",
        },
        {
          card1: 3,
          id: 3,
          title: "Third Title",
          text: "third",
        },
        {
          card1: 4,
          id: 4,
          title: "Fourth Title",
          text: "fourth",
        },
      ],
    };
  },
}
</script>
