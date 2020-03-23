from django.http import HttpResponse
from django.shortcuts import render

# 图片管理
def tpgl(request):
    return render(request,'tupian_pc_index.html')

# 系统管理
def syset(request):
    return render(request,'xitong_set.html')