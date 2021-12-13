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
              <el-col style="text-align: center" :xs="24" :lg="4">
                <el-image
                  v-if="screenWidth > 500"
                  style="height: 70px; width: 70px; margin-top: 2px"
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
              <el-col class="text-item" :xs="24" :lg="8">
                <span> {{ item.title }} </span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="6">
                <span style="padding-left: 100px">
                  发布者：{{ item.nickName }}
                </span>
              </el-col>
              <el-col class="text-item" :xs="12" :lg="6">
                <el-button
                  @click="toArticle(item.id)"
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
  inject: ['reload'],
  data() {
    return {
      currentPage: 1,
      pageSize: 5,
      total: 100,
      article_list: [],
    };
  },
  beforeRouteEnter (to, from, next) {
    // console.log("zizujianbeforeRouteEnter")
    to.meta.keepAlive = true
    if (from.path != '/article') {
      next(vm => {
        vm.reload()
      })
    } else {
      next()
    }
  },
  beforeRouteLeave(to, from, next) {
    if (to.path != "/article") {
      from.meta.keepAlive = false;
    } else {
      from.meta.keepAlive = true;
    }
    next();
  },
  mounted() {
    // console.log("mounted");
    this.getListData(this.currentPage);
  },
  methods: {
    //跳转内容页
    toArticle(id) {
      this.$router.push({ path: "/article", query: { id: id } });
    },
    getListData(page) {
      axios({
        method: "get",
        url: "http://127.0.0.1:9000/api/article-list/",
        params: {
          page,
          pageSize: this.pageSize,
          lanmu: "all",
        },
      }).then((res) => {
        // console.log(res.data);
        this.article_list = res.data.data;
        this.total = res.data.total;
      });
    },
    currentChange(val) {
      console.log("第" + val + "页");
      this.currentPage = val;
      this.getListData(val);
    },
    //删除文章
    deleteArticle(id) {
      if (confirm("是否确定删除")) {
        let checkInfo = {
          contentType: "blog_article",
          permissions: ["delete"],
        };
        this.$store.dispatch("checkUserPerm", checkInfo).then((res) => {
          console.log(res);
          if (res) {
            axios({
              method: "delete",
              url: "http://127.0.0.1:9000/api/delete-article/",
              data: Qs.stringify({
                id,
                token: this.$store.getters.isnotUserlogin,
              }),
              headers: {
                "Content-Type": "application/x-www-form-urlencoded",
              },
            }).then((res) => {
              console.log(res);
              if (res.data == "nologin") {
                alert("用户信息错误");
                return;
              }
              if (res.data == "noperm") {
                alert("权限不足");
              }
              this.getListData(this.currentPage);
            });
          }
        });
      }
    },
  },
};
</script>

<style scoped>
#article-list .blogshader {
  padding: 1px 10px;
}
.card.blogshader .text-item {
  height: 80px;
  color: #fff;
  display: flex;
  justify-content: center;
  text-align: center;
  align-items: center;
  font-size: 13px;
  text-overflow: ellipsis;
  overflow: hidden;
  /* background-color: brown; */
}
</style>