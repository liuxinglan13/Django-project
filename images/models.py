from django.db import models
from users.models import User


class Image(models.Model):
    user = models.ForeignKey(User, related_name='images_created')
    title = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title
