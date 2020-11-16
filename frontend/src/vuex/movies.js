// import SERVER from "@/api/drf.js"

export default {
  namespaced: true,
  state: {
    movieList: null,
  },
  getters: {
  
  },
  mutations: {
    SET_MOVIE_LIST(state, movieList) {
      state.movieList = movieList
    }
  },
  actions: {}
}