import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login.vue'
import Movies from './views/Movies.vue'
// vue-cookies 
import cookies from "vue-cookies"
// lazy-loading 
const Signup = () => import(/* webpackChunkName: "Signup" */ './views/Signup.vue')

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Movies',
    name: 'Movies',
    component: Movies
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    beforeEnter(from, to, next) {
      const islogin = cookies.get("auth-token")
      if (!islogin) {
        next()
      } else {
        alert("로그인 한 상태에서는 할 수 없습니다.")
        next('/')
      }
    }
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
    beforeEnter(from, to, next) {
      const islogin = cookies.get("auth-token")
      if (!islogin) {
        next()
      } else {
        alert("로그인 한 상태에서는 할 수 없습니다.")
        next('/')
      }
    }
  }
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
