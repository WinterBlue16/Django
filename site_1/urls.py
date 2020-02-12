from django.contrib import admin
from django.urls import path
from lotto import views

urlpatterns = [
    # 127.0.0.1:8000/admin/
    path('admin/', admin.site.urls), #저기서 들어오면 이 함수가 실행됨
    # 127.0.0.1:8000/
    path('', views.index),
    # 127.0.0.1:8000/hello/
    path('hello/', views.hello, name='hello_main'),
    # 127.0.0.1:8000/lotto/
    path('lotto/', views.index, name='index'),
    path('lotto/new', views.post, name='new_lotto'),
    path('lotto/<int:lottokey>/detail', views.detail, name='detail'),
]
