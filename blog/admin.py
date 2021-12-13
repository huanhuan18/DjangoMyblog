from django.contrib import admin
from blog.models import Article, Userinfo, Lanmu, Favorite, Like, PayOrder

# Register your models here.
admin.site.register(Article)
admin.site.register(Userinfo)
admin.site.register(Lanmu)
admin.site.register(Favorite)
admin.site.register(Like)
admin.site.register(PayOrder)
