import Vue from 'vue'
import App from './App.vue'
import router from './routes'
import store from "./vuex/index"
import vuetify from './plugins/vuetify'
import VueCookies from 'vue-cookies'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'


Vue.config.productionTip = false

Vue.use(VueCookies)
// set default config of 1 hour
Vue.$cookies.config('1h')

// fontawesome
Vue.component('font-awesome-icon', FontAwesomeIcon)
library.add(fab)


new Vue({
  store,
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
