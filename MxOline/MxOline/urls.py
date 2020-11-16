#coding:utf-8
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import TemplateView
from apps.users.views import LoginView, LogoutView, SendSmsView, DyanmicLoginView, RegisterView
from django.views.decorators.csrf import csrf_exempt  #去除csrf_token验证

import xadmin
#xadmin会发现我们自己注册的UserProfile并把它注册到后台，admin如果覆盖了user表则不会注册到后台


urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('dynamic_login/',DyanmicLoginView.as_view(),name='dynamic_login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('captcha/', include('captcha.urls')),
    path('send_sms/', csrf_exempt(SendSmsView.as_view()), name='send_sms'),
]


#1.CBV(class base view)   FBV(function base view)
#2.编写一个view的几个步骤
'''
view代码
配置url
修改html页面中的相关地址
'''
