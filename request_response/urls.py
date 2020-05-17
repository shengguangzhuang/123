from django.urls import path,re_path
from . import views




urlpatterns = [

    #测试提取查询字符串参数：http：//127.0.0.1:8000/querystring/?name=zxc&age=18
    path('querystring/',views.QSParamView.as_view()),
    # http://127.0.0.1:8000/formdata/
    path('formdata/',views.FormDataParamView.as_view()),
    # http://127.0.0.1:8000/sgzjson/
    path('sgzjson/',views.JsonView.as_view()),
    # Url_Param2
    path('url_param2/<mobile:phone_num>/',views.Url_Param2.as_view()),

    re_path(r'^Re_path/(?P<phone_num>1[3-9]\d{9})/$',views.Re_path.as_view()),
]