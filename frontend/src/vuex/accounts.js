import axios from "axios"
import SERVER from "@/api/drf.js"
import cookies from "vue-cookies"

export default {
  namespaced: true,
  state: {
    authToken: cookies.get("auth-token")
  },
  getters: {
    isLogin: state => !!state.authToken,
    config: state => ({ headers: { Authorization: `Token ${state.authToken}` } })
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.authToken = token
      cookies.set("auth-token", token)
    }
  },
  actions: {
    postAuthData({ commit }, info) {
      console.log(info.data)
      axios.post(info.location, info.data)
        .then(res => {
          console.log(res)
          commit("SET_TOKEN", res.data.token)
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
    logout() {
      cookies.remove("auth-token")
    }
  }
}