#coding:utf-8
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.views.generic import TemplateView
from apps.users.views import LoginView, LogoutView, SendSmsView, DyanmicLoginView, RegisterView
from django.views.decorators.csrf import csrf_exempt  #去除csrf_token验证

from django.views.static import serve
from MxOline.settings import MEDIA_ROOT
# from MxOline.settings import STATIC_ROOT
import xadmin
#xadmin会发现我们自己注册的UserProfile并把它注册到后台，admin如果覆盖了user表则不会注册到后台
from apps.operations.views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('',IndexView.as_view(),name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('dynamic_login/',DyanmicLoginView.as_view(),name='dynamic_login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('captcha/', include('captcha.urls')),
    path('send_sms/', csrf_exempt(SendSmsView.as_view()), name='send_sms'),

    #配置上传文件的访问url
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),

    # 测试403/404/500的url
    # url(r'^static/(?P<path>.*)$', serve, {"document_root":STATIC_ROOT}),

    #机构相关页面
    # path('org_list/', OrgView.as_view(),name='org_list'),
    url(r'^org/', include(('apps.organizations.urls', 'organizations'), namespace='org')),

    #课程相关页面
    url(r'^course/', include(('apps.courses.urls', 'courses'), namespace='course')),

    #用户相关操作
    url(r'^op/', include(('apps.operations.urls', 'operations'), namespace='op')),

    # 个人中心
    url(r'^users/', include(('apps.users.urls', 'users'), namespace='users')),
]


#1.CBV(class base view)   FBV(function base view)
#2.编写一个view的几个步骤
'''
view代码
配置url
修改html页面中的相关地址
'''
