import axios from "axios"
import SERVER from "@/api/drf"

export default {
  postAuthData({ commit }, info) {
    axios.post(info.location, info.data) 
      // need to add additional session logic 
      .then((res) => {
        commit("SET_TOKEN", res.data.token)
      })
      .catch((err) => console.log(err))
  },
  login({ dispatch }, loginData) {
    const info = {
      location: SERVER.URL + SERVER.ROUTES.login,
      data: loginData
    }
    dispatch("postAuthData", info)
  },
  logout({ getters, commit }) {
    axios.post(SERVER.URL + SERVER.ROUTES.logout, null, getters.config)
    .then(() => {
      commit("SET_TOKEN", null)

    })
    .catch((err) => console.log(err))
  },
  signup({ dispatch }, signupData) {
    const info = {
      location: SERVER.URL + SERVER.ROUTES.signup,
      data: signupData
    }
    dispatch("postAuthData", info)
  }
}