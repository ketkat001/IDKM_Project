export default {
  isLogin: state => !!state.authToken,
  config: state => ({ headers: { Authorization: `Token ${state.authToken}` } })
}