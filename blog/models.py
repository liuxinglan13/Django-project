from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# Category 分类


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Tag 标签


class Tag(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

# Post 文章


class Post(models.Model):

    # 文章标题
    title = models.CharField(max_length=70)

    def __str__(self):
        return self.title

    # 这个方法用来生产url
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    # 文章正文
    body = models.TextField()

    # 文章的创建和最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 将上面创建的分类和标签与文章联系起来
    # 我们规定 一篇文章只能对应一个分类 但一个分类下可以有多篇文章 所以是一对多的关系 ForeignKey 代表一对多
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系
    # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(User)

