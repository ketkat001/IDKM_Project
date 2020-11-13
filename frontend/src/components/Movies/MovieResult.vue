<template>
  <div class="movie-result">
    <h1>이런 영화를 찾으셨나요?</h1>
    <div class="result-cards row">
      <MovieCard v-for="card in cardList" :key="card.id" :card="card" />
    </div>
  </div>
</template>

<script>
import "@/assets/css/components/movies/movieResult.scss";
import MovieCard from "@/components/Movies/MovieCard.vue";

export default {
  name: "MovieResult",
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
};
</script>
