import Vue from "vue"
import Vuex from "vuex"
import createPersistedState from "vuex-persistedstate"
import accounts from "./accounts.js"
import movies from "./movies.js"
Vue.use(Vuex)

const modules = {
  accounts,
  movies
}

export default new Vuex.Store ({
  modules,
  plugins: [createPersistedState({
    paths: ["accounts", "movies"]
  }
  )]
})