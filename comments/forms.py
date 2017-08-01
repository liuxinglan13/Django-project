from django import forms
from .models import Comment

# 这是评论的表单


class CommentForm(forms.ModelForm):
    class Meta:
    # model 代表 该表单是绑定那个数据模型
        model = Comment

    # fields 这个元祖 代表要展现填写的表单 字段
        fields = ['text']
