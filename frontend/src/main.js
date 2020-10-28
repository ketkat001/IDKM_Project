import Vue from 'vue'
import App from './App.vue'
import router from './routes'
import store from "./vuex/index"
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

// RegExp of email 
// var emailRE = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/

new Vue({
  store,
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
