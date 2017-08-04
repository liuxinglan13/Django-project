# 这个文件 是 自定义模板标签
# 使用的地方是类似 base.html之类的模版  用来替换模版标签 填充内容
from ..models import Post, Category, Tag
from django import template
from django.db.models.aggregates import Count

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
# 以下方法输出两个属性   Category.name    所有的分类名
#                        Category.num_posts   相应分类名下的文章的总数
# 使用了 模型管理器 objects 的 annotate 方法
@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

# 标签云
# 1
@register.simple_tag
def get_tag():
    return Tag.objects.all()
