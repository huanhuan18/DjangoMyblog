<template>
  <div id="login-page">
    <video id="v1" autoplay loop muted>
      <source src="../assets/img/whale_fall.mp4" type="video/mp4" />
    </video>
    <label class="sentence1">我们的征途是，</label>
    <label class="sentence2">星辰大海</label>

    <div class="blogshader loginbox">
      <div class="header">
        <h2>Login</h2>
        <!-- <el-divider></el-divider> -->
      </div>
      <el-form :label-position="'right'" label-width="50px" :model="formData">
        <!-- <el-form-item label="UserName">
            <el-input class="input_item" v-model="formData.username"></el-input>
          </el-form-item> -->
        <div class="item">
          <input type="text" v-model="formData.username" />
          <label for="">UserName</label>
        </div>
        <!-- <el-form-item label="PassWord">
            <el-input v-model="formData.password"></el-input>
          </el-form-item> -->
        <div class="item">
          <input type="password" v-model="formData.password" />
          <label for="">PassWord</label>
        </div>
        <el-form-item>
          <button @click="blogLogin()" class="login_btn">
            submit
            <span></span>
            <span></span>
            <span></span>
            <span></span>
          </button>
          <button @click="toRegister()" class="register_btn">register</button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
// import "../assets/js/canvas_font.js";

// import axios from "axios";
// import Qs from "qs";
export default {
  data() {
    return {
      formData: {
        username: "guest",
        password: "guest123123",
      },
    };
  },
  //局部路由
  //   beforeRouteEnter (to, from, next) {
  //       console.log("局部路由跳转"+from.path)
  //       next()
  //   },
  mounted() {},
  methods: {
    blogLogin() {
      if (
        this.formData.username.length == 0 ||
        this.formData.password.length == 0
      ) {
        alert("表单填写完整");
        return;
      }
      //   axios({
      //     url: "http://127.0.0.1:9000/api/gf-login/",
      //     method: "post",
      //     data: Qs.stringify(this.formData),
      //   }).then((res) => {
      //     if (res.data == "none") {
      //       alert("用户名不存在");
      //       return;
      //     }
      //     if (res.data == "pwderr") {
      //       alert("密码错误");
      //       return;
      //     }
      //     console.log(res.data);
      //     this.$store.commit("saveUserinfo", res.data);
      //   });
      //上面注释的是第一种方法，下面将请求放到store下的index.js内的actions中的第二种方法
      this.$store.dispatch("blogLogin", this.formData);
    },
    toRegister() {
      this.$router.push({ path: "register" });
    },
  },
};
</script>

<style scoped>
#login-page {
  /* height: 60vh;
  width: 430px;
  margin-left: 40vw; */
  display: flex;
  align-items: center;
  justify-content: center;
  /* background-color: rgb(255, 0, 21); */
}
.backgroud-moon {
  position: fixed;
  /* background-color: #2be2138e; */
  background: url("../assets/img/sea.gif") no-repeat;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  z-index: 99;
  /* transform: rotate(-90deg); */
  background-size: 100% 100%;
}

.sentence1 {
  float: left;
  position: absolute;
  left: -150px;
  top: 50px;
  font-size: 50px;
  /* 两层背景，一层与被背景色相同，一层与文字色相同 */
  background-color: transparent;
  color: #1974c9;
  opacity: 0;
  text-shadow: 5px 5px 0 #666, 7px 7px 0 #eee;
  animation: show_name1 20s ease-out  infinite;
  z-index: 13;
}
@keyframes show_name1 {
  0% {
    opacity: 0;
  }
  20% {
    opacity: 0.5;
  }
  86% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}
.sentence1::before {
  content: "我们的征途是,";
  color: transparent;
  position: absolute;
  background-image: linear-gradient(
    to right,
    red,
    orange,
    yellow,
    green,
    blue,
    indigo,
    violet
  );
  background-clip: text;
  -webkit-background-clip: text;
  clip-path: polygon(-20% 0%, 0% 0%, -10% 100%, -30% 100%);
  animation: move1 6s 2s infinite;
}
@keyframes move1 {
  0% {
    clip-path: polygon(-20% 0%, 0% 0%, -10% 100%, -30% 100%);
  }
  50% {
    clip-path: polygon(110% 0%, 130% 0%, 120% 100%, 100% 100%);
  }
  100% {
    clip-path: polygon(-20% 0%, 0% 0%, -10% 100%, -30% 100%);
  }
}
.sentence2 {
  float: left;
  position: absolute;
  list-style: none;
  left: -30px;
  top: 130px;
  font-size: 50px;
  color: #f3dc8efb;
  opacity: 0;
  text-shadow: 5px 5px 0 #666, 7px 7px 0 #eee;
  animation: show_name2 20s ease-out infinite;
  /* animation: show_name 6s ease-out 2s 1 forwards; */
  z-index: 13;
}
@keyframes show_name2 {
  0% {
    opacity: 0;
  }
  35% {
    opacity: 0;
  }
  86% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}

.sentence2::before {
  content: "星辰大海";
  color: transparent;
  position: absolute;
  background-image: linear-gradient(
    to right,
    red,
    orange,
    yellow,
    green,
    blue,
    indigo,
    violet
  );
  background-clip: text;
  -webkit-background-clip: text;
  clip-path: polygon(-20% 0%, 0% 0%, -10% 100%, -30% 100%);
  animation: move2 6s 6s infinite;
}
@keyframes move2 {
  0% {
    clip-path: polygon(-20% 0%, 0% 0%, -10% 100%, -30% 100%);
  }
  50% {
    clip-path: polygon(110% 0%, 130% 0%, 120% 100%, 100% 100%);
  }
  100% {
    clip-path: polygon(-20% 0%, 0% 0%, -10% 100%, -30% 100%);
  }
}

/* 视频样式 */
video {
  position: fixed;
  right: 0px;
  bottom: 0px;
  min-width: 100%;
  min-height: 100%;
  height: auto;
  width: auto;
  /*加滤镜*/
  /*filter: blur(15px); //背景模糊设置 */
  /*-webkit-filter: grayscale(100%);*/
  /*filter:grayscale(100%); //背景灰度设置*/
  z-index: 11;
}
source {
  min-width: 100%;
  min-height: 100%;
  height: auto;
  width: auto;
}
.loginbox {
  position: absolute;
  width: 245px;
  height: 280px;
  top: 180px;
  right: 140px;
  padding: 10px;
  font-size: 14px;
  z-index: 13;
  /* transform: rotate(90deg); */
}
input,
button {
  background: transparent;
  border: none;
  outline: none;
}
/* 输入框 */
.item {
  height: 37px;
  border-style: none;
  border-bottom: 1px solid #fff;
  margin-bottom: 20px;
  position: relative;
}
.item input {
  width: 100%;
  height: 100%;
  color: #fff;
  /* 让输入框的文字离底线近一点 */
  padding-top: 20px;
  box-sizing: border-box;
}
.item input:focus + label {
  top: 0px;
  font-size: 12px;
}
.item label {
  color: #03e9f4;
  position: absolute;
  left: 0;
  top: 12px;
  transition: all 0.5s linear;
}

/* 登录按钮 */
.login_btn {
  /* width: 100px;
  height: 36px; */
  /* padding: 0px 20px 20px 20px; */
  margin-top: 20px;
  margin-left: -20px;
  color: #03e9f4;
  overflow: hidden;
  background-color: transparent;
  position: relative;
  text-transform: uppercase;
  letter-spacing: 2px;
}
.register_btn {
  margin-left: 40px;
  color: #03e9f4;
  position: relative;
}
.register_btn:hover {
  background: #03e9f4;
  border-radius: 5px;
  color: #fff;
  box-shadow: 0 0 5px #03e9f4, 0 0 25px #03e9f4, 0 0 50px #03e9f4,
    0 0 10px #03e9f4;
}
.login_btn:hover {
  background: #03e9f4;
  border-radius: 5px;
  color: #fff;
  box-shadow: 0 0 5px #03e9f4, 0 0 25px #03e9f4, 0 0 50px #03e9f4,
    0 0 10px #03e9f4;
}
.login_btn > span {
  position: absolute;
}
.login_btn > span:nth-child(1) {
  width: 100%;
  height: 2px;
  background: -webkit-linear-gradient(left, transparent, #03e9f4);
  left: -100%;
  top: 0;
  /* linear表示匀速运动，infinite表示无限循环 */
  animation: line1 1s linear infinite;
}
@keyframes line1 {
  50%,
  100% {
    left: 100%;
  }
}
.login_btn > span:nth-child(2) {
  width: 2px;
  height: 100%;
  background: -webkit-linear-gradient(top, transparent, #03e9f4);
  right: 0;
  top: -100%;
  animation: line2 1s 0.25s linear infinite;
}
@keyframes line2 {
  50%,
  100% {
    top: 100%;
  }
}
.login_btn > span:nth-child(3) {
  width: 100%;
  height: 2px;
  background: -webkit-linear-gradient(right, transparent, #03e9f4);
  left: 100%;
  bottom: 0;
  animation: line3 1s 0.5s linear infinite;
}
@keyframes line3 {
  50%,
  100% {
    left: -100%;
  }
}
.login_btn > span:nth-child(4) {
  width: 2px;
  height: 100%;
  background: -webkit-linear-gradient(bottom, transparent, #03e9f4);
  left: 0;
  top: 100%;
  animation: line4 1s 0.75s linear infinite;
}
@keyframes line4 {
  50%,
  100% {
    top: -100%;
  }
}
</style>