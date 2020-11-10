import Vue from "vue"
import Vuex from "vuex"
import createPersistedState from "vuex-persistedstate"
import accounts from "./accounts.js"

Vue.use(Vuex)

const modules = {
  accounts
}

export default new Vuex.Store ({
  modules,
  plugins: [createPersistedState({
    paths: ["accounts"]
  }
  )]
})