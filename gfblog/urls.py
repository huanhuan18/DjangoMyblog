"""gfblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import api_url

# drf_yasg2 从这里开始
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Tweet API",
        default_version='v1',
        description="Welcome to the world of Tweet",
        terms_of_service="https://www.tweet.org",
        contact=openapi.Contact(email="demo@tweet.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # re_path(r'^doc(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- 这里
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  #<-- 这里
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  #<-- 这里
    path('admin/', admin.site.urls),
    path('api/', include(api_url)),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
