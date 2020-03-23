from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from UserLogin.func import pv

# 首页
def index(request):
    return render(request,'index.html')

# 首页头部分
def public_header(request):
    return render(request,'public_header.html')

# 首页左边分类栏
def publeft(request):
    return render(request,'public_left.html')

# 登陆
def login(request):
    return render(request,'loginb.html')
    # return render(request,'1.html')

# 修改密码
def changepsw(request):
    return render(request,'change_psw.html')

# 生成图片验证码
def pageyz(request):
    print("".center(50,"8"))
    result = pv.generate()
    # 把验证码字符串保存到session
    # request.session['code'] = pv.code
    # 创建响应对象
    res = HttpResponse(result,'image/png')
    # res.content_type = 'image/png'
    return res