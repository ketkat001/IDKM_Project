export default {
  URL: 'http://127.0.0.1:8000',
  R: {
    ACCOUNTS: {
      login: '/accounts/auth/login/',
      logout: '/rest-auth/logout/',
      signup: '/accounts/auth/register/',
      check: '/accounts/check/'
    },
    MOVIES: {
      movie: '/movies/',
      movieSearch: '/movies/search/',
      movieDetail: '/movie/',
      movieRecommend: '/movies/recommend/'
    }
  }
}