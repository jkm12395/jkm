# author:1zt
# date: 2020/2/14 10:01
# file_name: urls
# 引入路由
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^detail/(\d+)', views.detail),
    url(r'^about/$', views.about)
]
