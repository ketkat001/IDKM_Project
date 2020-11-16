<template>
  <div class="home-wrapper">
    <div class="home-content">
      <div class="main-search d-flex flex-column">
        <div class="home-logo">
          <a class="logo-homepage" href=""></a>
        </div>
        <div class="home-search">
          <v-text-field
            class="search-input"
            name="input"
            placeholder="생각나는 영화의 내용을 적어주세요"
            append-icon="mdi-magnify"
            hide-details
            v-model="searchInput"
            @keyup.enter="searchMovie()"
          >
          </v-text-field>
        </div>
      </div>
      <div class="main-board d-flex">
        <div class="board-content">
          <h1 class="main-title">
            보고 싶은 영화의 제목이 생각이 나지 않을때는?
            <span> IDONTKNOWMOVIE 와 함께 찾아봐요!</span>
          </h1>
        </div>
      </div>
      <div class="main-info">
        <div class="info-items d-flex">
          <div class="info-items-wrap d-flex">
            <div class="info-item d-flex flex-column">
            </div>
            <div class="info-item d-flex flex-column">
            </div>
            <div class="info-item d-flex flex-column">
            </div>
          </div>
        </div>
        <svg class="main-info-curve" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1438 134">
          <path d="M1438 1442H0V31.001S438.105 0 719 .001c280.896 0 719 31 719 31V1442z" fill="currentColor"></path>
        </svg>
      </div>
    </div>
    <div class="main-slide">
        
    </div>
  </div>
  
</template>

<script>
import "@/assets/css/views/home.scss";
import SERVER from "@/api/drf.js"
import axios from "axios"
import { mapState, mapMutations } from "vuex"

export default {
  name: 'Home',
  mounted() {
    this.SET_MOVIE_LIST(null)
    this.movieRecommend()
  },
  computed: {
    ...mapState("accounts", ["user"])
  },
  methods: {
    ...mapMutations("movies", ["SET_MOVIE_LIST"]),
    searchMovie() {
      axios
        .get(SERVER.URL + SERVER.R.MOVIES.movieSearch + "?query=" + this.searchInput)
        .then((res) => {
          // console.log(res.data)
          this.SET_MOVIE_LIST(res.data)
          this.$router.push('/movies/')
        })
    },
    movieRecommend() {
      const URL = SERVER.URL + SERVER.R.MOVIES.recommend + this.user.id
      axios.get(URL)
      .then(res => console.log(res))
      .catch(err => console.log(err))
    }
  },
  data() {
    return {
      searchInput: "",
    }
  }
}
</script>
