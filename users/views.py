from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import UserDetailForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


# 用户注册的视图函数

def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、确认密码、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    # 将记录用户注册前页面的 redirect_to 传给模板，以维持 next 参数在整个注册流程中的传递
    return render(request, 'users/register.html', context={'form': form, 'next': redirect_to})

# 编辑用户资料

@login_required
def account_profile(request):
    messages = []
    # post请求 表明是在修改用户资料
    if request.method == 'POST':
        # 使用getattr可以获得一个querydict，里面包含提交的内容
        request_dic = getattr(request, 'POST')
        print(request_dic)
        print(request.FILES)
        print(request.user.avatar.url)
        form = UserDetailForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            print('修改资料完成')
            form.save()
    # 如果是get请求，则使用user生成表单
    form = UserDetailForm(instance=request.user)
    return render(request, 'users/user_detail.html', context={'form':form,
                                                                'messages':messages,})


