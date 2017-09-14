from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    avatar = ProcessedImageField(upload_to='avatar',
                                 default='avatar/default.png',
                                 verbose_name='头像',
                                 # 图片将处理成85x85的尺寸
                                 processors=[ResizeToFill(150, 150)], )
    print(avatar)

    # def save(self, *args, **kwargs):
    #     # 当用户更改头像的时候，avatar.name = '文件名'
    #     # 其他情况下avatar.name = 'upload_to/文件名'
    #     if len(self.avatar.name.split('/')) == 1:
    #         # print('before:%s' % self.avatar.name)
    #         # 用户上传图片时，将avatar.name改为 用户名/文件名
    #         self.avatar.name = self.username + '/' + self.avatar.name
    #     super(User, self).save()
    #     # 调用父类的save()方法后，avatar.name就变成了'upload_to/用户名/文件名'
    #     # print('after:%s' % self.avatar.name)
    #     # print('avatar_path: %s' % self.avatar.path)

    # def get_user_avatar(self):
    #     if user.socialaccount_set.exists():
    #         # 绑定了社交账户
    #         return user.socialaccount_set.first().get_avatar_url()
    #     return self.avatar.url  # 假设存储用户头像的 Field 为 avatar（通常为 ImageField）

    # 这个方法用来调取 社交化头像
    def avatar_url(self):
        # 判断 如果没有修改过默认头像 自动调用社交头像 如果自己自己修改过头像来就不调用来
        avatar_name = self.avatar.name.rsplit('/', 1)[-1]
        if avatar_name == 'default.png':
            # 首先尝试从社交账户中获取头像
            if self.socialaccount_set.exists():
                return self.socialaccount_set.first().get_avatar_url()

        return self.avatar.url
