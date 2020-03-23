from django.urls import path

from UserLogin import views

app_name = 'UserLogin'
urlpatterns = [
    # 首页
    path('index/',views.index,name='index'),
    # 首页头部
    path('header/', views.public_header, name='pubh'),

    # 首页左边分类栏
    path('publeft/',views.publeft,name='publft'),
    # 登陆页面
    path('login',views.login,name='login'),
    # 修改密码
    path('changepwd/',views.changepsw,name='changepsw'),
    # 图形验证码
    path('pageyz/', views.pageyz, name='pageyz'),

]