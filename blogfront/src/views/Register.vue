<template>
  <div id="register-page">
    <video id="v1" autoplay loop muted>
      <source src="../assets/img/whale_fall.mp4" type="video/mp4" />
    </video>
    <label class="sentence1">我们的征途是，</label>
    <label class="sentence2">星辰大海</label>

    <div class="blogshader loginbox">
      <div class="header">
        <h4>新用户注册</h4>
        <!-- <el-divider></el-divider> -->
      </div>
      <el-form :label-position="'right'" label-width="70px" :model="formData">
        <!-- <el-form-item label="用户名">
          <el-input v-model="formData.username"></el-input>
        </el-form-item> -->
        <div class="item">
          <input type="text" v-model="formData.username" />
          <label for="">用户名</label>
        </div>
        <!-- <el-form-item label="密码">
          <el-input v-model="formData.password"></el-input>
        </el-form-item> -->
        <div class="item">
          <input type="password" v-model="formData.password" />
          <label for="">密码</label>
        </div>
        <!-- <el-form-item label="重复密码">
          <el-input v-model="formData.password2"></el-input>
        </el-form-item> -->
        <div class="item">
          <input type="password" v-model="formData.password2" />
          <label for="">重复密码</label>
        </div>
        <div class="item icode">
          <input type="text" v-model="formData.identcode" />
          <label for="">验证码</label>
        </div>
        <div class="get-code" @click="refreshCode()">
          <s-identify :identifyCode="identifyCode"></s-identify>
        </div>
        <el-form-item>
          <!-- <el-button @click="blogRegister()" type="success">注册</el-button>
          <el-button @click="toLogin()" type="warning" plain
            >已有账号</el-button
          > -->
          <button @click="blogRegister()" class="login_btn">
            注 册
            <span></span>
            <span></span>
            <span></span>
            <span></span>
          </button>
          <button @click="toLogin()" class="register_btn">已有账号></button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
// import Qs from "qs";
import SIdentify from "../components/SIdentify.vue";
export default {
  components: { SIdentify },
  data() {
    return {
      identifyCode: "",
      identifyCodes: "0123456789abcdwerwshdjeJKDHRJHKOOPLMKQ", //绘制的随机数
      formData: {
        username: "",
        password: "",
        password2: "",
        identcode: "",
      },
    };
  },
  created() {
    this.refreshCode();
  },
  methods: {
    // 验证码
    refreshCode() {
      this.identifyCode = "";
      this.makeCode(this.identifyCodes, 4);
    },
    randomNum(min, max) {
      max = max + 1;
      return Math.floor(Math.random() * (max - min) + min);
    },
    // 随机生成验证码字符串
    makeCode(data, len) {
      for (let i = 0; i < len; i++) {
        this.identifyCode += data[this.randomNum(0, data.length - 1)];
      }
    },
    toLogin() {
      this.$router.push({ path: "login" });
    },
    blogRegister() {
      if (
        this.formData.username.length == 0 ||
        this.formData.password.length == 0 ||
        this.formData.password.length == 0
      ) {
        alert("表单尚未填写完整");
        return;
      }
      if (this.formData.password != this.formData.password2) {
        alert("两次密码不一致");
        return;
      }
      if (this.formData.password.length < 8) {
        alert("密码太短");
        return;
      }
      if (
        this.formData.identcode.toLowerCase() != this.identifyCode.toLowerCase()
      ) {
        alert("验证码错误");
        this.refreshCode();
        return;
      }
      //提交注册
      //   axios({
      //     method: "post",
      //     url: "http://127.0.0.1:9000/api/gf-register/",
      //     data: Qs.stringify(this.formData),
      //   }).then((res) => {
      //     if (res.data == "repeat") {
      //       alert("用户名已存在");
      //       return;
      //     }
      //     console.log(res.data);
      //     this.$store.commit("saveUserinfo", res.data);
      //   });
      this.$store.dispatch("blogRegister", this.formData);
    },
  },
};
</script>

<style scoped>
/* #register-page {
  height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
} */
#register-page {
  /* height: 80vh;
  min-width: 500px;
  margin-left: 40vw; */
  display: flex;
  align-items: center;
  justify-content: center;
  /* background-color: aqua; */
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
  animation: show_name1 20s ease-out infinite;
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
  height: 370px;
  top: 160px;
  right: 140px;
  padding: 10px;
  font-size: 13px;
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

.icode {
  display: inline-block;
  width: 120px;
  padding: 0;
  margin-right: 5px;
}
.get-code {
  display: inline-block;
  padding: 0;
}

/* 登录按钮 */
.login_btn {
  /* width: 100px;
  height: 36px; */
  /* padding: 0px 20px 20px 20px; */
  margin-top: 8px;
  margin-left: -30px;
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