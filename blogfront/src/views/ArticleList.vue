<template>
  <div id="article-list">
    <!-- 面包屑导航 -->
    <div class="blogshader">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>文章列表</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <!-- 文章列表 -->
    <div class="blogshader" style="margin-top: 10px">
      <el-row>
        <el-col v-for="item in article_list" :key="item.id" :span="24">
          <div class="card blogshader">
            <el-row>
              <el-col :xs="24" :lg="6">
                <el-image
                  v-if="screenWidth > 500"
                  style="height: 100px"
                  :src="item.cover"
                  :fit="'cover'"
                ></el-image>
                <el-image
                  v-else
                  style="width: 100%"
                  :src="item.cover"
                  :fit="'cover'"
                ></el-image>
              </el-col>
              <el-col class="text-item" :xs="24" :lg="4">
                <span> {{ item.title }} </span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="7">
                <span> 发布者：{{ item.nickName }} </span>
              </el-col>
              <el-col :xs="12" :lg="7">
                <el-button
                  type="success"
                  icon="el-icon-search"
                  circle
                ></el-button>
                <el-button
                  type="danger"
                  icon="el-icon-delete"
                  circle
                  @click="deleteArticle(item.id)"
                ></el-button>
              </el-col>
            </el-row>
          </div>
        </el-col>
        <!-- <el-col :span="24">
          <div class="card blogshader">
            <el-row>
              <el-col :xs="24" :lg="6">
                <el-image
                  v-if="screenWidth > 500"
                  style="height: 100px"
                  :src="require('../assets/img/article1.png')"
                  :fit="'cover'"
                ></el-image>
                <el-image
                  v-else
                  style="width: 100%"
                  :src="require('../assets/img/article1.png')"
                  :fit="'cover'"
                ></el-image>
              </el-col>
              <el-col class="text-item" :xs="24" :lg="4">
                <span> 国家电网:全力守住民生用电底线 </span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="7">
                <span> 发布者：admin </span>
              </el-col>
              <el-col :xs="12" :lg="7">
                <el-button
                  type="success"
                  icon="el-icon-search"
                  circle
                ></el-button>
                <el-button
                  type="danger"
                  icon="el-icon-delete"
                  circle
                ></el-button>
              </el-col>
            </el-row>
          </div>
        </el-col> -->
      </el-row>
    </div>
    <!-- 分页器 -->
    <div class="blogshader" style="margin-top: 10px">
      <el-pagination
        background
        layout="prev, pager, next"
        :total="total"
        :page-size="pageSize"
        @current-change="currentChange"
      >
      </el-pagination>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Qs from "qs";
export default {
  props: ["screenWidth"],
  data() {
    return {
      currentPage: 1,
      pageSize: 3,
      total: 100,
      article_list: [],
    };
  },
  mounted() {
    this.getListData(this.currentPage);
  },
  methods: {
    getListData(page) {
      axios({
        method: "get",
        url: "http://127.0.0.1:9000/api/article-list/",
        params: {
          page,
          pageSize: this.pageSize,
        },
      }).then((res) => {
        console.log(res.data);
        this.article_list = res.data.data;
        this.total = res.data.total;
      });
    },
    currentChange(val) {
      console.log("第" + val + "页");
      this.currentPage = val
      this.getListData(val);
    },
    //删除文章
    deleteArticle(id) {
      if (confirm('是否确定删除')) {
        axios({
        method: "delete",
        url: "http://127.0.0.1:9000/api/delete-article/",
        data: Qs.stringify({
          id,
          token: this.$store.getters.isnotUserlogin,
        }),
        headers:{
          "Content-Type": "application/x-www-form-urlencoded",
        }
      }).then((res) => {
        console.log(res);
        if (res.data=='nologin') {
          alert("用户信息错误")
          return
        }
        this.getListData(this.currentPage)
      });
      }
    },
  },
};
</script>

<style scoped>
#article-list .blogshader {
  padding: 20px 10px;
}
.card.blogshader .text-item {
  height: 80px;
  color: #fff;
  display: flex;
  justify-content: center;
}
</style>