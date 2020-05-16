from django.shortcuts import render

# Create your views here.
#以下代码用于定义函数视图


# def register('请求对象'):
#     return '响应对象'


from django.views import View
from django import http

def register(request):
    return http.HttpResponse('假装这是个注册页面')


class RegisterView(View):

    def get(self, request):
        '''处理get模块
            :param request：请求
            :return：响应
        '''
        return http.HttpResponse('这里假装返回一个注册页面')

    def post(self, request):
        '''处理post模块
            :param request：请求
            :return：响应
        '''
        return http.HttpResponse('这里假装实现注册逻辑')