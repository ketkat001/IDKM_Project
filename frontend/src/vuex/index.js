import Vue from "vue"
import Vuex from "vuex"
import state from "./state"
import getters from "./getters"
import actions from "./actions"
import mutations from "./mutations"
import createPersistedState from "vuex-persistedstate"
import accounts from "./accounts.js"

Vue.use(Vuex)

const modules = {
  accounts
}

export default new Vuex.Store ({
  state,
  getters,
  actions,
  mutations,
  modules,
  plugins: [createPersistedState({
    paths: ["accounts"]
  }
  )]
})