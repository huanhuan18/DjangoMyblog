from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# 用户信息
class Userinfo(models.Model):
    headImg = models.ImageField()
    nickName = models.CharField()
    belong = models.OneToOneField(User)

    def __int__(self):
        return self.id


# 分类
class Category(models.Model):
    name = models.CharField()
    belong = models.ForeignKey(self)
    def __int__(self):
        return self.id

# 文章
class Article(models.Model):
    title = models.CharField()
    cover = models.CharField()
    text = models.TextField()
    belong = models.ForeignKey(Userinfo)

    def __int__(self):
        return self.id


# 收藏
class Favorite(models.Model):
    belong_user = models.ForeignKey(Userinfo)
    belong_art = models.ForeignKey(Article)

    def __int__(self):
        return self.id


# 点赞
class Like(models.Model):
    belong_user = models.ForeignKey(Userinfo)
    belong_art = models.ForeignKey(Article)

    def __int__(self):
        return self.id


# 打赏
class PayOrder(models.Model):
    order = models.CharField()
    price = models.CharField()
    status = models.BooleanField()