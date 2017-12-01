# _*_ coding: utf-8 _8_
import xadmin
from .models import Post, Category, Tag
from xadmin import views


class GlobalSettings(object):
    site_title = "后台管理系统"
    site_footer = "后台管理系统"
    menu_style = "accordion"        # 设置收起菜单


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


# Register your models here.
class PostAdmin(object):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    search_fields = ['title', 'category', 'author']
    list_filter = ['title', 'category', 'author']


xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Category)
xadmin.site.register(Tag)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)