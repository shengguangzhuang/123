# 必须定义一个路由样式列表
# 名字必须叫 ： urlpatterns
# 以上两个是必须的条件

from django.urls import path,re_path
from .import views
from django.conf.urls import url

# urlpatterns = [
#
# #     使用路由匹配请求地址，每匹配一个就执行对应的函数视图逻辑
#     path('网络地址正则表达式',视图函数)
# ]
urlpatterns = [
    #     使用路由匹配请求地址，每匹配一个就执行对应的函数视图逻辑
    path('user/register', views.register),]
# urlpatterns = [
#f
#     #     使用路由匹配请求地址，每匹配一个就执行对应的函数视图逻辑
#     # 在给类视图注册子路由时还需要将类视图转为函数视图
#     path('user/register', views.RegisterView.as_view()),
# ]

'''====================re_path子路由创建================================='''
# urlpatterns = [
# #     函数视图re_path（）路由写法
# #     re_path(r'^网络地址正则表达式$',函数视图名)
# #
# #     类视图re_path的写法：
# #      re_path(r'^网络地址正则表达式’$,类视图.as_view()),
#
# #     用户登入：http://127.0.0.1:8000/uers/login/
#     re_path(r'^user/login/$',views.LoginView.as_view()),
# ]
""""=====================url子路由创建================================="""
# urlpatterns = [
#     # 函数视图url()路由写法
#     # url(r'^网络地址正则表达式$',函数视图名),
#     #
#     # 类视图url()路由写法
#     # url(r'^网络地址正则表达式$'类视图.as_view()),
#     #
#     # 用户登录：http://127.0.0.1:8000/user/login/
#     url(r'^user/login/$',views.LoginView.as_view()),
#
#
# ]


