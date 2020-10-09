<template>
  <div id="app">
    <!-- 头部导航 -->
    <div id="top-menu" class="blogshader"></div>
    <!-- 侧边栏 左 导航 -->
    <div id="left-menu" class="blogshader"></div>
    <!-- 页面内容 -->
    <div id="content">
      <el-row :gutter="20">
        <el-col :span="8"
          ><div class="blogshader" style="height: 250px"></div
        ></el-col>
        <el-col :span="8"
          ><div class="blogshader" style="height: 250px"></div
        ></el-col>
        <el-col :span="8"
          ><div class="blogshader" style="height: 250px"></div
        ></el-col>
      </el-row>
      <el-row :gutter="20">
        <el-col :span="8"
          ><div class="blogshader" style="height: 250px"></div
        ></el-col>
        <el-col :span="8"
          ><div class="blogshader" style="height: 250px"></div
        ></el-col>
        <el-col :span="8"
          ><div class="blogshader" style="height: 250px"></div
        ></el-col>
      </el-row>
      <el-row :gutter="20">
        <el-col :span="8"
          ><div class="blogshader" style="height: 250px"></div
        ></el-col>
        <el-col :span="8"
          ><div class="blogshader" style="height: 250px"></div
        ></el-col>
        <el-col :span="8"
          ><div class="blogshader" style="height: 250px"></div
        ></el-col>
      </el-row>

      <!-- 页面底部 -->
      <div id="footer" class="blogshader">
        <span>Copyright@gf的个人博客</span>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      value: true,
    };
  },
};
</script>


<style>
.el-col {
  margin-top: 5px;
}
</style>
