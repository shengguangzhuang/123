# 必须定义一个路由样式列表
# 名字必须叫 ： urlpatterns
# 以上两个是必须的条件

from django.urls import path
from .import views

#
# urlpatterns = [
#
#
# #     使用路由匹配请求地址，每匹配一个就执行对应的函数视图逻辑
#     path('网络地址正则表达式',视图函数)
# ]
#
# urlpatterns = [
#
#     #     使用路由匹配请求地址，每匹配一个就执行对应的函数视图逻辑
#
#     path('user/register', views.register),
# ]


# 、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、#



urlpatterns = [

    #     使用路由匹配请求地址，每匹配一个就执行对应的函数视图逻辑
    # 在给类视图注册子路由时还需要将类视图转为函数视图
    path('user/register', views.RegisterView.as_view()),
]


