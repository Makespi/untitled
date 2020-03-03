from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect


def home(request):
    return HttpResponse('<h1>Hello</h1>')


def login(request):
    error_msg = ""
    # 获取用户的提交方式
    if request.method == "POST":
        usr = request.POST.get("usr", None)
        pwd = request.POST.get("pass", None)
        print(usr, pwd)
        if usr == "admin" and pwd == "12":
            return redirect(request, 'success.html')
        else:
            error_msg = "用户名密码错误"
    return render(request, 'login.html', {'error_msg': error_msg})
# Create your views here.
