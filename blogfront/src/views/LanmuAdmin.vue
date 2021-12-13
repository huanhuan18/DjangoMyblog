<template>
  <div>
    <!-- 面包屑导航 -->
    <BreadMenu :page_name="'栏目管理'"></BreadMenu>

    <!-- 内容 -->
    <div class="body blogshader">
      <el-row :gutter="10">
        <el-col :span="6">
          <div class="blogshader">
            <h5>栏目结构</h5>
            <el-divider></el-divider>
          </div>
          <div class="body blogshader" style="display: flex">
            <el-input
              v-model="new_lanmu_name"
              placeholder="请输入新栏目名称"
            ></el-input>
            <el-button @click="pushLanmuList()" type="success">保存</el-button>
          </div>

          <div class="body blogshader">
            <el-tree
              :data="lanmu_tree"
              node-key="id"
              default-expand-all
              draggable
              :render-content="renderContent"
              @node-click="choosed_lanmu_articleList"
            >
            </el-tree>
          </div>
          <div class="save-tree body blogshader" style="float: left">
            <el-button @click="getLanmuTree()" type="warning" size="mini"
              >恢复结构</el-button
            >
            <el-button @click="saveLanmuTree()" type="success" size="mini"
              >保存结构</el-button
            >
            <el-button @click="getListData(1, 'all')" type="primary" size="mini"
              >全部文章获取</el-button
            >
          </div>
        </el-col>
        <el-col :span="18">
          <div class="blogshader">
            <h5>文章列表</h5>
            <el-divider></el-divider>
          </div>

          <!-- 文章列表 -->
          <div class="blogshader" style="margin-top: 10px; min-height: 468px">
            <el-row>
              <el-col v-for="item in article_list" :key="item.id" :span="24">
                <div class="card blogshader">
                  <el-row>
                    <el-col :xs="24" :lg="4">
                      <el-image
                        style="height: 80px; width: 100px"
                        :src="item.cover"
                        :fit="'cover'"
                      ></el-image>
                    </el-col>
                    <el-col class="text-item" :xs="24" :lg="8">
                      <a href="" @click="toArticle(item.id, $event)">
                        <span> {{ item.title }} </span>
                      </a>
                    </el-col>
                    <el-col class="text-item" :xs="12" :lg="6">
                      <span style="padding-left: 80px">
                        发布者：{{ item.nickName }}
                      </span>
                    </el-col>
                    <el-col class="text-item" :xs="12" :lg="6">
                      <el-popover placement="right" width="90" trigger="click">
                        <el-tree
                          :data="lanmu_tree"
                          node-key="id"
                          default-expand-all
                          @node-click="choosed_lanmu"
                        >
                        </el-tree>
                        <el-button
                          type="warning"
                          icon="el-icon-plus"
                          circle
                          slot="reference"
                        ></el-button>
                        <el-button
                          type="success"
                          size="mini"
                          @click="saveArticleToLanmu(item.id)"
                          >确定</el-button
                        >
                      </el-popover>
                    </el-col>
                  </el-row>
                </div>
              </el-col>
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
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import BreadMenu from "../components/BreadMenu";
import axios from "axios";
import Qs from "qs";
export default {
  //接收刷新
  inject: ["reload"],
  data() {
    return {
      //文章内容
      currentPage: 1,
      currentLanmu: "nobelong",
      pageSize: 4,
      total: 100,
      article_list: [],
      //栏目结构
      maxId: 0,
      new_lanmu_name: "",
      lanmu_tree: [],
      //文章栏目分配
      choosed_lanmu_id: 0,
      choosed_article_id: 0,
    };
  },
  //不是从article页进来的就刷新缓存
  beforeRouteEnter(to, from, next) {
    to.meta.keepAlive = true;
    if (from.path != "/article") {
      next((vm) => {
        vm.reload();
      });
    } else {
      next();
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
    this.getListData(this.currentPage, this.currentLanmu);
    this.getLanmuTree();
  },
  methods: {
    //跳转内容页
    toArticle(id, event) {
      event.preventDefault();
      this.$router.push({ path: "/article", query: { id: id } });
    },
    //选择栏目查看文章
    choosed_lanmu_articleList(node) {
      let lanmu_name = node.label;
      this.getListData(1, lanmu_name);
    },
    //选择文章保存栏目
    choosed_lanmu(node) {
      console.log(node);
      this.choosed_lanmu_id = node.id;
      this.choosed_lanmu_name = node.label;
    },
    saveArticleToLanmu(article_id) {
      axios({
        method: "put",
        url: "http://127.0.0.1:9000/api/add-article/",
        data: Qs.stringify({
          token: this.$store.getters.isnotUserlogin,
          lanmu_id: this.choosed_lanmu_id,
          article_id: article_id,
        }),
      }).then((res) => {
        if (res.data == "nologin") {
          alert("尚未登录");
          return;
        }
        if (res.data == "noperm") {
          alert("权限不足");
          return;
        }
        if (res.data == "ok") {
          console.log(res.data);
          this.getListData(1, this.choosed_lanmu_name);
          this.getLanmuTree();
        }
      });
    },
    //获取栏目数据
    getLanmuTree() {
      axios({
        method: "get",
        url: "http://127.0.0.1:9000/api/gf-lanmu/",
      }).then((res) => {
        console.log(res.data);
        this.lanmu_tree = res.data;
      });
    },

    //保存栏目结构
    saveLanmuTree() {
      console.log(this.lanmu_tree);
      axios({
        method: "put",
        url: "http://127.0.0.1:9000/api/gf-lanmu/",
        data: Qs.stringify({
          token: this.$store.getters.isnotUserlogin,
          lanmu_tree: JSON.stringify(this.lanmu_tree),
        }),
      }).then((res) => {
        console.log(res.data);
        if (res.data == "nologin") {
          alert("尚未登录");
          return;
        }
        if (res.data == "noperm") {
          alert("权限不足");
          return;
        }
      });
    },
    //新栏目名称
    pushLanmuList() {
      let checkTree = this.loopCheckData(this.lanmu_tree);
      console.log(checkTree);
      if (checkTree == false) {
        this.new_lanmu_name = "";
        return;
      }
      let new_lanmu = {
        id: this.maxId + 1,
        label: this.new_lanmu_name,
        children: [],
      };
      console.log(new_lanmu);
      this.lanmu_tree.push(new_lanmu);
      this.new_lanmu_name = "";
    },
    loopCheckData(tree) {
      let checkTree = true;
      //检查新栏目数据
      tree.forEach((obj) => {
        if (obj.id > this.maxId) {
          this.maxId = obj.id;
        }
        if (obj.label == this.new_lanmu_name) {
          alert("命名重复");
          checkTree = false;
          return;
        }
        if (obj.children) {
          if (obj.children.length > 0) {
            this.loopCheckData(obj.children);
          }
        }
      });

      return checkTree;
    },
    getListData(page, lanmu) {
      axios({
        method: "get",
        url: "http://127.0.0.1:9000/api/article-list/",
        params: {
          page,
          pageSize: this.pageSize,
          lanmu: lanmu,
        },
      }).then((res) => {
        // console.log(res.data + "+当前栏目" + this.currentLanmu);
        this.article_list = res.data.data;
        this.total = res.data.total;
        this.currentLanmu = lanmu;
      });
    },
    currentChange(val) {
      // console.log("第" + val + "页");
      this.currentPage = val;
      this.getListData(val, this.currentLanmu);
    },
    remove(node, data) {
      // console.log(data.id);
      if (confirm("是否确认删除？")) {
        axios({
          method: "delete",
          url: "http://127.0.0.1:9000/api/gf-lanmu/",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
          data: Qs.stringify({
            token: this.$store.getters.isnotUserlogin,
            id: data.id,
          }),
        }).then((res) => {
          // console.log(res.data);
          if (res.data == "nologin") {
            this.getListData(this.currentPage, this.currentLanmu);
            this.getLanmuTree();
            alert("尚未登录");
            return;
          }
          if (res.data == "noperm") {
            this.getListData(this.currentPage, this.currentLanmu);
            this.getLanmuTree();
            alert("权限不足");
            return;
          }
          if (res.data == "ok") {
            this.getLanmuTree();
          }
        });
      } else {
        this.getListData(this.currentPage, this.currentLanmu);
        this.getLanmuTree();
      }
    },
    renderContent(h, { node, data }) {
      return (
        <span class="custom-tree-node">
          <span>{node.label}</span>
          <span> ({node.data.article_num})</span>
          <span style="position:absolute;right:10px">
            <el-button
              size="mini"
              type="text"
              on-click={() => this.remove(node, data)}
            >
              删除
            </el-button>
          </span>
        </span>
      );
    },
  },
  components: {
    BreadMenu,
  },
};
</script>

<style scoped>
.custom-tree-node {
  position: relative;
}
.blogshader {
  padding: 8px 10px;
  font-size: 13px;
}
.card.blogshader .text-item {
  height: 80px;
  color: #fff;
  display: flex;
  justify-content: center;
  text-align: center;
  align-items: center;
  font-size: 13px;
}
a {
  max-height: 80px;
  line-height: 20px;
  font-size: 13px;
  text-decoration-line: none;
  color: #fff;
  text-overflow: ellipsis;
  overflow: hidden;
}
a:hover {
  color: rgb(16, 176, 240);
}
.text-item span {
  text-align: center;
  display: block;
}
.save-tree button {
  margin: 5px 5px;
}
</style>