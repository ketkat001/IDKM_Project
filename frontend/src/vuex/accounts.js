import axios from "axios"
import SERVER from "@/api/drf.js"
import cookies from "vue-cookies"
import router from "../routes"

export default {
  namespaced: true,
  state: {
    authToken: cookies.get("auth-token"),
    user: null
  },
  getters: {
    isLogin: state => !!state.authToken,
    config: state => ({ headers: { Authorization: `Token ${state.authToken}` } })
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.authToken = token
      cookies.set("auth-token", token)
    },
    SET_USER(state, user) {
      state.user = user
    }
  },
  actions: {
    postAuthData({ commit }, info) {
      // console.log(info.data)
      axios.post(info.location, info.data)
      .then(res => {
        // console.log(res)
        commit("SET_USER", res.data.user)
        commit("SET_TOKEN", res.data.token)
        router.push({ name: 'Home' })
      })
      .catch(err => console.log(err))
    },
    signup({ dispatch }, signupData) {
      const info = {
        location: SERVER.URL + SERVER.R.ACCOUNTS.signup,
        data: signupData
      }
      dispatch("postAuthData", info)
    },
    login({ dispatch }, loginData) {
      const info = {
        location: SERVER.URL + SERVER.R.ACCOUNTS.login,
        data: loginData
      }
      dispatch("postAuthData", info)
    },
    logout({ commit }) {
      console.log('You are logged out')
      commit("SET_TOKEN", null)
      commit("SET_USER", null)
    }
  }
}