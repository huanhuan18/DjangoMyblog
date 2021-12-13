from django.urls import path
from blog import api, payapi

urlpatterns = [
    # 文章管理
        # 文章数据获取 查看
        path('article-data/', api.articleData),
        # 文章发布
        path('article-list/', api.articleList),
        # 文章修改页
        path('article-edit/', api.articleEdit),
        # 文章修改
        path('update-article/', api.articleUpdate),
        # 文章列表
        path('add-article/', api.add_article),
        # 文章删除
        path('delete-article/', api.deleteArticle),
    # 用户管理
        # 登录
        path('gf-login/', api.gf_login),
        # 注册
        path('gf-register/', api.gf_register),
        # 自动登录
        path('auto-login/', api.gf_autoLogin),
        # 登出
        path('gf-logout/',api.gf_logout),
        # 鉴权
        path('gf-checkperm/', api.gf_checkPerm),
        # 用户列表
        path('gf-userlist/', api.gf_userlist),
    # 用户组
        path('gf-group/', api.gf_group),
    # 栏目管理
        path('gf-lanmu/', api.gf_lanmu),
    # 文章用户互动
        path('pinglun/', api.gf_pinglun),
        path('user-article-info/', api.userArticleInfo),
        path('article-like/', api.articleLike),
        path('article-favor/', api.articleFavor),
        path('get-alipay-url/', payapi.getAlipayUrl)
]