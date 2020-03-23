from django.urls import path

from App import views
app_name = 'App'

urlpatterns = [
    # 首页
    path('index/',views.index,name='index'),

    # 框架
    # 右边标题栏
    path('header/', views.public_header, name='header'),
    # 左边导航栏
    path('left/', views.public_left, name='left'),

    # 主窗口，内容展示
    path('main/', views.public_main, name='main'),
    path('main/<int:cid>',views.public_main, name='main'),
    path('main/<int:cid>/<int:page>',views.public_main, name='main2'),


]