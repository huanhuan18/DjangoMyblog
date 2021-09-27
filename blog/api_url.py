from django.urls import path
from blog import api

urlpatterns = [
    path('add-article/', api.add_article),
    # 用户管理
    # 登录
    path('gf-login/', api.gf_login),
    # 注册
    path('gf-register/', api.gf_register),
    # 自动登录
    path('auto-login/', api.gf_autoLogin),
    # 登出
    path('gf-logout/',api.gf_logout)
]