## 这是一个用户登录和注册教学项目
## 这是一个可重用的登录和注册APP
## 该项目教程发布在www.liujiangblog.com

## 简单的使用方法：


创建虚拟环境
使用pip安装第三方依赖
修改settings.example.py文件为settings.py
运行migrate命令，创建数据库和数据表
运行python manage.py runserver启动服务器


路由设置：


from django.contrib import admin
from django.urls import path, include
from login import views

urlpatterns = [\n
    path('admin/', admin.site.urls), \n
    path('index/', views.index),\n
    path('login/', views.login),\n
    path('register/', views.register),\n
    path('logout/', views.logout),\n
    path('confirm/', views.user_confirm),\n
    path('captcha/', include('captcha.urls'))  \n # 增加这一行
]
