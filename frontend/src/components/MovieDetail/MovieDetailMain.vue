<template>
  <section class="movie-main-content">
    <div class="content-wrap">
      <div class="movie-overview">
        <h2>줄거리</h2>
        <p>얼굴을 보면 그 사람의 모든 것을 꿰뚫어보는 천재 관상가 내경. 처남 ‘팽헌’, 아들 ‘진형’과 산속에 칩거하고 있던 그는 관상 보는 기생 ‘연홍’의 제안으로 한양으로 향하고, 연홍의 기방에서 사람들의 관상을 봐주는 일을 하게 된다. 용한 관상쟁이로 한양 바닥에 소문이 돌던 무렵, ‘내경’은 ‘김종서’로부터 사헌부를 도와 인재를 등용하라는 명을 받아 궁으로 들어가게 되고, ‘수양대군’이 역모를 꾀하고 있음을 알게 된 그는 위태로운 조선의 운명을 바꾸려 한다.</p>
      </div>
      <div class="side-main">
        <div class="movie-side-poster">
          <img src="https://movie-phinf.pstatic.net/20130819_110/1376895907326wlXma_JPEG/movie_image.jpg" width="272" height="408" class="real">
        </div>
      </div>
      <div class="movie-actors">
        <h2>주요 출연진</h2>
        <div class="actor-list row">
          <ActorCard class="actor-card" v-for="card in cardList" :key="card.id" :card="card"/>
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
  data() {
    return {
      cardList:  [
        {
          card1: 1,
          id: 1,
          title: "First Title",
        },
        {
          card1: 2,
          id: 2,
          title: "Second Title",
        },
        {
          card1: 3,
          id: 3,
          title: "Third Title",
        },
        {
          card1: 4,
          id: 4,
          title: "Fourth Title",
        },
      ],
    }
  }
}
</script>
