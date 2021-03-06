from django.urls import path
from booktest import views

# 应用中url配置严格匹配开头和结尾
urlpatterns = [
    # 通过url函数设置url路由配置项
    path('index', views.index),
    path('index2', views.index2),
    path('books', views.show_books),
    path('books/<int:bid>', views.detail)

]
