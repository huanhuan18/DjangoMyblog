import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  //登录
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  //注册
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/add-article',
    name: 'AddArticle',
    component: () => import('../views/AddArticle.vue')
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]
// const routerPush = VueRouter.prototype.push
// VueRouter.prototype.push = function push(location) {
//   return routerPush.call(this,location)
// }

const router = new VueRouter({
  routes
})

export default router
