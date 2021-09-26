<template>
  <div id="login-page">
    <div class="blogshader loginbox">
      <div class="header">
        用户登录
        <el-divider></el-divider>
      </div>
      <el-form :label-position="'right'" label-width="60px" :model="formData">
        <el-form-item label="用户名">
          <el-input v-model="formData.username"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="formData.password"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button @click="blogLogin()" type="success">登录</el-button>
          <el-button @click="toRegister()" type="warning" plain
            >前往注册</el-button
          >
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
// import Qs from "qs";
export default {
  data() {
    return {
      formData: {
        username: "",
        password: "",
      },
    };
  },
  //局部路由
//   beforeRouteEnter (to, from, next) {
//       console.log("局部路由跳转"+from.path)
//       next()
//   },
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
  height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
.loginbox {
  padding: 10px;
}
</style>