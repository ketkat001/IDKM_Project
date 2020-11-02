import axios from "axios"
import router from "@/routes.js"
import SERVER from "@/api/drf"

export default {
  postAuthData({ commit }, info) {
    axios.post(info.location, info.data) 
      // need to add additional session logic 
      .then((res) => console.log(res))
      .catch((err) => console.log(err))
  },
  login({ dispatch }, loginData) {
    const info = {
      location: SERVER.URL + SERVER.ROUTES.login,
      data: loginData
    }
    dispatch("postAuthData", info)
  },
  logout( { getters, commit }) {
    axios.post(SERVER.URL + SERVER.ROUTES.logout, null, getters.config)
    .then(() => {
      commit("SET_TOKEN", null)

    })
    .catch((err) => console.log(err))
  }
}