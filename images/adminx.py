from .models import Image
import xadmin


class ImageAdmin(object):
    list_display = ['title', 'image', 'created']
    list_filter = ['created']


xadmin.site.register(Image, ImageAdmin)