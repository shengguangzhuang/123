"""DjangoBase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path ,include
from django.urls import register_converter
from converters import MobileConverter

# urlpatterns = [
#     path('admin/', admin.site.urls),
#
#
#     path('',include('user.urls')),
#     path('',include('request_response.urls')),
# ]
# 注册自定义路由转换器
# register_converters(自定义路由转换器,'别名')
register_converter(MobileConverter,'mobile')

urlpatterns = [

    path('',include('request_response.urls')),
]