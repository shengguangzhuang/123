from django.shortcuts import render
from django.views import View
from django import http
import json

# Create your views here.

'''==============================字符串参数==================='''
class QSParamView(View):
    """测试提取查询字符串参数
    http://127.0.0.1:8000/querystring/?name=zxc&age=18

    """
    def get(self, request):

        name = request.GET.get('name')
        age = request.GET.get('age')

        print(name,age)

        return http.HttpResponse('测试提取查询字符串参数：%s--%s'%(name,age))

'''=================================表单================'''

class FormDataParamView(View):
    """测试提取表单类型请求提参数
    http://127.0.0.1:8000/formdata/
    """
    def post(self,request):

        # formdata = request.POST
        # username = formdata.get('username')
        # password = formdata.get('password')
        username = request.POST.get("username")
        password = request.POST.get('password')
        print(username,password)

        return http.HttpResponse('表单参数:%s--%s' % (username,password))
'''=========================json============================================'''

class JsonView(View):


    def post(self,requst):


        json_dict = json.loads(requst.body)
        username = json_dict.get('username')
        password = json_dict.get('password')

        print(username,password)

        return http.HttpResponse('json参数:%s--%s' % (username,password))

'''===================================路径参数=================================='''


class Url_Param2(View):

    def get(self,request,phone_num):


        return http.HttpResponse('测试电话号码：%d' % phone_num)


'''=======================================re_path=========================='''

class Re_path(View):

    def get(self,request,phone_num):


        return http.HttpResponse('测试re_path:%s'% phone_num)
