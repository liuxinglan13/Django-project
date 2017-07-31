from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
    # 主要匹配 detail.html 中 <form action="{% url 'comments:post_comment' post.pk %}" method="post" class="comment-form">
    # comments:post_comment' post.pk  这部分 这个表单提交数据时 产生这样的（/comment/post/10/）URL 下面匹配这个URL调用相应函数试图处理
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]