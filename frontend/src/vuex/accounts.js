export default {
  namespaced: true;
  state: {
    authToken: null
  },
  getters: {
    isLogin: state => !!state.authToken,
    config: state => ({ headers: { Authorization: `Token ${state.authToken}` } })
  },
  mutations: {
    SET_TOKEN({ commit }, token) {

    }
  },
  actions: {

  }
}