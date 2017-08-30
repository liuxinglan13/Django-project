from django import forms
from .models import Post
from django.forms import TextInput, Select


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'tags')
        # 重写（覆盖）默认的字段 http://python.usyiyi.cn/translate/django_182/topics/forms/modelforms.html
        # 给title 添加了一个 css class类名
        widgets = {
            'title': TextInput(attrs={'class':'form-control'}),
            'category':Select(attrs={'class': 'form-control'}),
        }






