from django.shortcuts import render

# Create your views here.
#以下代码用于定义函数视图


# def register('请求对象'):
#     return '响应对象'

from django import http

def register(request):
    return http.HttpResponse('假装这是个注册页面')