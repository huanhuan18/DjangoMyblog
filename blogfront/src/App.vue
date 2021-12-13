<template>
  <div id="app">
    <!-- 头部导航 -->
    <div id="top-menu" class="blogshader">
      <div class="usericon">
        <span class="name">{{ username }}</span>
        <img class="userinfo-avatar" src="./assets/img/article1.png" />
      </div>
    </div>
    <!-- 侧边栏 左 导航 -->
    <div id="left-menu" :class="'blogshader ' + mobile_left">
      <i @click="showHideLeftMenu" id="left-btn" class="el-icon-menu"></i>
      <!-- 导航栏 -->
      <el-col :span="24" style="margin-top: 80px">
        <!-- 任意6个数字再加2个0为透明色 -->
        <el-menu
          class="el-menu-vertical-demo"
          background-color="#00000000"
          text-color="#fff"
          active-text-color="#ffd04b"
          router
          :default-openeds="['1']"
          @select="ChooseMenu"
        >
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>文章管理</span>
            </template>
            <el-menu-item-group>
              <el-menu-item
                index="/add-article"
                style="padding-left: 50px; min-width: 180px"
                >发布文章</el-menu-item
              >
              <el-menu-item
                index="article-list"
                style="padding-left: 50px; min-width: 180px"
                >文章列表</el-menu-item
              >
            </el-menu-item-group>
          </el-submenu>
          <el-menu-item index="user-permission">
            <i class="el-icon-user"></i>
            <span slot="title">用户管理</span>
          </el-menu-item>
          <el-menu-item index="dashang-record">
            <i class="el-icon-money"></i>
            <span slot="title">打赏记录</span>
          </el-menu-item>
          <el-menu-item index="lanmu-admin">
            <i class="el-icon-s-operation"></i>
            <span slot="title">栏目管理</span>
          </el-menu-item>
          <el-menu-item v-if="authUserLogin" @click="blogLogout()">
            <i class="el-icon-back"></i>
            <span slot="title">退出登录</span>
          </el-menu-item>
        </el-menu>
      </el-col>
    </div>
    <!-- 页面内容 -->
    <div id="content" :class="mobile_content">
      <keep-alive v-if="isRouterAlive">
        <router-view :screenWidth="screenWidth" v-if="$route.meta.keepAlive">
          <!-- 这里是被缓存的视图组件 -->
        </router-view>
      </keep-alive>
      <router-view v-if="!$route.meta.keepAlive" :screenWidth="screenWidth">
        <!-- 这里是不被缓存的视图组件 -->
      </router-view>

      <!-- 页面底部 -->
      <div id="footer" class="blogshader">
        <span style="font-size: 15px">Copyright ©朱朱好学</span>
        <br />
        <a style="font-size: 13px" href="http://beian.miit.gov.cn/"
          >皖ICP备2021016447号-1</a
        >
      </div>
    </div>
  </div>
</template>


<script>
var fnTextPopup = function (arr) {
  // arr参数是必须的
  if (!arr || !arr.length) {
    return;
  }
  // 主逻辑
  var index = 0;
  document.documentElement.addEventListener("click", function (event) {
    var x = event.pageX,
      y = event.pageY;
    var eleText = document.createElement("span");
    eleText.className = "text-popup";
    this.appendChild(eleText);
    if (arr[index]) {
      eleText.innerHTML = arr[index];
    } else {
      index = 0;
      eleText.innerHTML = arr[0];
    }
    // 动画结束后删除自己
    eleText.addEventListener("animationend", function () {
      eleText.parentNode.removeChild(eleText);
    });
    // 位置
    eleText.style.left = x - eleText.clientWidth / 2 + "px";
    eleText.style.top = y - eleText.clientHeight + "px";
    // index递增
    index++;
  });
};

fnTextPopup([
  "富强",
  "民主",
  "文明",
  "和谐",
  "自由",
  "平等",
  "公正",
  "法治",
  "爱国",
  "敬业",
  "诚信",
  "友善",
]);
export default {
  data() {
    return {
      screenWidth: document.body.clientWidth,
      mobile_left: "",
      mobile_content: "",
      username: "",
      isRouterAlive: true, //用来刷新keep-alive;通过provide向下面子孙组件们暴露一个reload方法，用来刷新缓存。
    };
  },
  provide() {
    return { reload: this.reload };
  },
  computed: {
    //验证用户是否登录
    authUserLogin() {
      return this.$store.getters.isnotUserlogin;
    },
    getUsername() {
      return this.$store.getters.getUserName;
    },
  },
  watch: {
    //监听用户token
    authUserLogin(newVal) {
      if (newVal == null) {
        this.$router.push({ path: "login" });
      }
    },
    //监听修改用户名
    getUsername(name) {
      this.username = name;
    },
  },
  created() {
    this.$store.dispatch("tryAutoLogin");
  },
  mounted() {
    //L2D看板娘
    setTimeout(() => {
      window.L2Dwidget.init({
        pluginRootPath: "live2dw/",
        pluginJsPath: "lib/",
        pluginModelPath: "live2d-widget-model-z16/assets/",
        tagMode: false,
        debug: false,
        model: {
          jsonPath: "../live2dw/live2d-widget-model-z16/assets/z16.model.json",
        },
        display: { position: "left", width: 100, height: 200 },
        mobile: { show: true },
        log: false,
      });
    }, 1000);
    // 监听网页宽度变化
    // window.onresize = () =>{
    //   this.screenWidth = document.body.clientWidth
    //   console.log(this.screenWidth)
    // }
    this.changeDevice();
  },
  methods: {
    //刷新缓存
    reload() {
      this.isRouterAlive = false;
      this.$nextTick(() => (this.isRouterAlive = true));
    },
    // toAddArticle() {
    //   this.$router.push({name:'AddArticle'})
    // },
    ChooseMenu(index) {
      console.log(index);
      // this.$router.push({path:index})  //关掉el-menu的router可启用该句
    },
    changeDevice() {
      if (this.screenWidth <= 500) {
        this.mobile_left = "xs";
        this.mobile_content = "xs";
      }
    },
    showHideLeftMenu() {
      if (this.mobile_left == "") {
        this.mobile_left = "xs";
      } else {
        this.mobile_left = "";
      }
      // 宽屏
      if (this.screenWidth > 500) {
        if (this.mobile_content == "") {
          this.mobile_content = "lg";
        } else {
          this.mobile_content = "";
        }
      }
    },
    //退出登录
    blogLogout() {
      // this.$store.commit('clearUserinfo')
      // this.$router.push({path:'/'})
      this.$store.dispatch("blogLogout", this.$store.getters.isnotUserlogin);
    },
  },
};
</script>


<style>
a {
  background-color: transparent;
  word-break: break-all;
  text-decoration: none;
  text-decoration-line: none;
  text-decoration-style: initial;
  text-decoration-color: initial;
  color: rgb(199, 29, 29);
  font-size: 15px;
}
a:hover {
  color: #ffffff;
}

.el-col {
  margin-top: 5px;
}
.usericon {
  /* background-color: brown; */
  padding: 1px;
  position: absolute;
  top: 5px;
  right: 20px;
  display: flex;
  justify-content: center;
  text-align: center;
}

/* 裁剪图片 */
.userinfo-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-left: 10px;
}
.name {
  display: block;
  width: 60px;
  margin: 1px 1px;
  line-height: 35px;
  color: #ffffff;
  font-weight: 200;
  font-size: 15px;
  overflow: hidden;
}
.text-popup {
  animation: textPopup 1s;
  color: red;
  user-select: none;
  white-space: nowrap;
  position: absolute;
  z-index: 99;
}
@keyframes textPopup {
  0%,
  100% {
    opacity: 0;
  }
  5% {
    opacity: 1;
  }
  100% {
    transform: translateY(-50px);
  }
}
</style>
