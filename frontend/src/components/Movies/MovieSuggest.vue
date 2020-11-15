<template>
  <div class="movie-suggest">
    <h1>그리고 당신을 위한 더 많은 영화가 있답니다!</h1>
    <div class="suggest-cards row">
      <MovieCard   v-for="card in cardList" :key="card.id" :card="card" />
    </div>
  </div>
</template>

<script>
import "@/assets/css/components/movies/movieSuggest.scss"
import MovieCard from "@/components/Movies/MovieCard.vue";

export default {
  name: "MovieSuggest",
  components: {
    MovieCard
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
        {
          card1: 5,
          id: 5,
          title: "Fifth Title",
          text: "Fifth",
        },
        {
          card1: 6,
          id: 6,
          title: "Sixth Title",
          text: "Sixth",
        },
        {
          card1: 7,
          id: 7,
          title: "Seventh Title",
          text: "Seventh",
        },
        {
          card1: 8,
          id: 8,
          title: "Eighth Title",
          text: "Eighth",
        },
      ],
    }
  }

}
</script>

<style>

</style>