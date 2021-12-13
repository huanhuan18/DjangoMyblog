import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import store from '../store'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    beforeEnter: (to, from, next) => {
      if (store.state.userinfo.token) {
        next()
      } else {
        next('/login')
      }
    }
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
  //发布文章
  {
    path: '/add-article',
    name: 'AddArticle',
    component: () => import('../views/AddArticle.vue'),
    beforeEnter: (to, from, next) => {
      if (store.state.userinfo.token) {
        next()
      } else {
        next('/login')
      }
    }
  },
  //修改文章
  {
    path: '/edit-article',
    name: 'EditArticle',
    component: () => import('../views/EditArticle.vue'),
    beforeEnter: (to, from, next) => {
      if (store.state.userinfo.token) {
        //判断用户权限
        let checkInfo = {
          'contentType': 'blog_article',
          'permissions': ['change']
          // 'permissions': ['add', 'change', 'delete', 'view']
        }
        store.dispatch("checkUserPerm", checkInfo).then((res) => {
          console.log(res)
          if (res) {
            next()
          }
        })
      } else {
        next('/login')
      }
    }
  },
  //文章列表
  {
    path: '/article-list',
    name: 'ArticleList',
    component: () => import('../views/ArticleList.vue'),
    meta: {
      // requireAuth: true, // 添加该字段，表示进入这个路由是需要登录的
      keepAlive: false, //此组件不需要被缓存
    },
    mode: 'history',
    scrollBehavior(to, from, savedPosition) {
      if (savedPosition) {
        return savedPosition
      } else {
        return {
          x: 0,
          y: 0
        }
      }
    },
    beforeEnter: (to, from, next) => {
      if (store.state.userinfo.token) {
        to.meta.keepAlive = true
        if (from.path == '/article') {
          to.meta.keepAlive = true
        }
        next()
      } else {
        next('/login')
      }
    }
  },
  //用户管理
  {
    path: '/user-permission',
    name: 'UserPerm',
    component: () => import('../views/UserPerm.vue'),
    beforeEnter: (to, from, next) => {
      //判断用户登录
      if (store.state.userinfo.token) {
        //判断用户权限
        let checkInfo = {
          'contentType': 'auth_user',
          'permissions': ['view']
          // 'permissions': ['add', 'change', 'delete', 'view']
        }
        store.dispatch("checkUserPerm", checkInfo).then((res) => {
          console.log(res)
          if (res) {
            next()
          }
        })
      } else {
        next('/login')
      }
    }
  },
  //打赏记录
  {
    path: '/dashang-record',
    name: 'DashangRecord',
    component: () => import('../views/DashangRecord.vue'),
    beforeEnter: (to, from, next) => {
      if (store.state.userinfo.token) {
        next()
      } else {
        next('/login')
      }
    }
  },
  //栏目管理
  {
    path: '/lanmu-admin',
    name: 'LanmuAdmin',
    component: () => import('../views/LanmuAdmin.vue'),
    meta: {
      keepAlive: false, //此组件不需要被缓存
    },
    beforeEnter: (to, from, next) => {
      //判断用户登录
      if (store.state.userinfo.token) {
        //缓存文章列表页，从文章页返回不刷新页面
        to.meta.keepAlive = true
        if (from.path == '/article') {
          to.meta.keepAlive = true
        }
        //判断用户权限
        let checkInfo = {
          'contentType': 'blog_lanmu',
          // 'permissions': ['add', 'change', 'delete', 'view']
          'permissions': ['view']
        }
        store.dispatch("checkUserPerm", checkInfo).then((res) => {
          console.log(res)
          if (res) {
            next()
          }
        })
      } else {
        next('/login')
      }
    }
  },
  //文章内容页
  {
    path: '/article',
    name: 'Article',
    component: () => import('../views/Article.vue'),
    beforeEnter: (to, from, next) => {
      //判断用户登录
      if (store.state.userinfo.token) {
        //判断用户权限
        let checkInfo = {
          'contentType': 'blog_article',
          'permissions': ['view']
        }
        store.dispatch("checkUserPerm", checkInfo).then((res) => {
          console.log(res)
          if (res) {
            next()
          }
        })
      } else {
        next('/login')
      }
    }
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/nologin',
    name: 'noLoginMain',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/noLoginMain.vue')
  }
]

const routerPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return routerPush.call(this, location)
}

const router = new VueRouter({
  routes
})

//全局路由
// router.beforeEach((to,from,next)=>{
//   console.log("to:"+to.path)
//   console.log("from:"+from.path)
//   next()
// })

export default router
