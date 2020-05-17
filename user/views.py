from django.shortcuts import render
from django.views import View
from django import http
# Create your views here.

'''===============================函数视图=========================='''
'''以下代码用于定义函数视图
def register('请求对象'):
    return '响应对象'
'''
def register(request):
    return http.HttpResponse('假装这是个注册页面')

'''================================类视图==========================='''
class RegisterView(View):

    """
    http://127.0.0.1/uers/register/

    """
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


'''==================re_path和url的用法=========================='''


class LoginView(View):
    '''用户登录视图
    http：//127.0.0.1:8000/user/login/'''

    def get(self, request):
        """
        处理get请求，返回登录页面
        :param request: 请求对象，包含了请求信息
        :return: 响应对象，用于构造响应报文，并响应给用户
        """
        return http.HttpResponse("这回是用来制造一个假的登录页面")

    def post(self, request):
        """
        处理post请求，实现逻辑登录
        :param request: 请求对象，包含请求报文信息
        :return: 响应对象，用于构造响应报文，并响应给用户
        """
        return http.HttpResponse('假装实现登录逻辑')
'''====================http传参的几种方式：字符串数据，表单数据和json和路径参数，电话号码======================'''



'''================================传字符串参数====================================='''