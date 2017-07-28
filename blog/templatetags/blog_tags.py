# 这个文件 是 自定义模板标签
from ..models import Post, Category
from django import template

register = template.Library()


# 这个方法用来获取 最新的文章  获取数据库中前mun篇文章
@register.simple_tag              # 将函数注册为模板
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


# 归档模板标签 就是按时间  年 月 日 将文章进行归档
# order='DESC' 降序排列
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


# 分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()