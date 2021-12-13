import Vue from 'vue'
import ElementUI from 'element-ui'
import App from './App.vue'
import store from './store'
import router from './router'
import 'element-ui/lib/theme-chalk/index.css';
import './assets/css/icon/iconfont.css'

//引入summernote
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.css'
import 'popper.js'
import 'summernote'
import 'summernote/lang/summernote-zh-CN.js'
import 'summernote/dist/summernote.css'

import './assets/css/mystyle.css'

//特效
// import './assets/js/sakura.js'
import './assets/js/snow3.js'


Vue.use(ElementUI)
Vue.config.productionTip = false
Vue.config.devtools = true;

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
