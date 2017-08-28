from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import ModelForm

# 用户注册的表单
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


# 编辑用户资料的表单

class UserDetailForm(ModelForm):
    class Meta:
       # 关联的数据库模型，这里是用户模型
        model = User
       # 前端显示、可以修改的字段
        fields = ('nickname', 'avatar')
