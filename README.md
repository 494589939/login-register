## 这是一个用户登录和注册教学项目
## 这是一个可重用的登录和注册APP
## 该项目教程发布在www.liujiangblog.com

## 简单的使用方法：


创建虚拟环境<br>
使用pip安装第三方依赖<br>
修改settings.example.py文件为settings.py<br>
运行migrate命令，创建数据库和数据表<br>
运行python manage.py runserver启动服务器<br>


路由设置：<br><br>


from django.contrib import admin <br>
from django.urls import path, include <br>
from login import views<br>
<br><br>
urlpatterns = [ <br>
    path('admin/', admin.site.urls), 
    path('index/', views.index),<br>
    path('login/', views.login),<br>
    path('register/', views.register),<br>
    path('logout/', views.logout),<br>
    path('confirm/', views.user_confirm),<br>
    path('captcha/', include('captcha.urls'))  # 增加这一行<br>
]
