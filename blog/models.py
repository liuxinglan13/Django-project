from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
import timeago
from ckeditor_uploader.fields import RichTextUploadingField
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
    # RichTextUploadingField()  是富文本编辑器ckeditor 的自定义控件
    body = RichTextUploadingField(verbose_name='正文')

    # views 字段记录阅读量
    # PositiveIntegerField，该类型的值只允许为正整数或 0，因为阅读量不可能为负值。初始化时 views 的值为 0。
    views = models.PositiveIntegerField(default=0)

    # increase_views 方法用来自动累加阅读量 每当有人访问该篇文章阅读量就+1
    # 注意这里使用了 update_fields 参数来告诉 Django 只更新数据库中 views 字段的值，以提高效率。
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    # 文章的摘要（可以为空 下面save方法用来 自动提取文章摘要-从正文body中提取）
    excerpt = models.CharField(max_length=200, blank=True)

    # 文章的创建和最后一次修改时间
    # auto_now_add 自动保存当前时间 进数据
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    # 将文章创建时间和当前时间做 timeago 处理 就是那种 几分钟前，几天前，几个月前那种效果  存储这个处理后的字段
    timeago = models.CharField(max_length=200, blank=True)

    def time_ago(self, created_time, date):
        self.timeago = timeago.format(created_time, date, 'zh_CN')
        self.save(update_fields=['timeago'])

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

    # 提出文章正文摘要的方法
    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]+'...'

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

    # 定义一个 Meta 的内部类，这个内部类通过指定一些属性来规定这个类该有的一些特性
    # 这里指定排序方式 为创建时间  逆序  定义了这个方法后 就是说之后 POST这个表查询出来的东西默认都是逆序排列
    class Meta:
        ordering = ['-created_time']

