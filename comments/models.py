from django.db import models

# Create your models here.
# 这是评论app 的 模型


# 定义 text评论的正文 created_time评论产生的时间
class Comment(models.Model):
    text = models.TextField()
    # 当评论数据保存到数据库时，自动把 created_time 的值指定为当前时间
    created_time = models.DateTimeField(auto_now_add=True)
    # 将评论和被评论的文章详情 联系起来 形成一个 一对多的关系
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]
