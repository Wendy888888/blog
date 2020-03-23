from django.urls import path

from PictureChange import views

app_name ='PictureChange'
urlpatterns =[
    # 图片管理
    path('tpgl/', views.tpgl, name='tpgl'),
    # 系统管理
    path('syset/', views.syset, name='syset'),

]