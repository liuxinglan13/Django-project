from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
import markdown
from comments.forms import CommentForm



# Create your views here.


def index(request):
    # - 表示逆序 不加则是正序
    post_list = Post.objects.all().order_by('-created_time')
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)

def detail(request, pk):
    # get_object_or_404 用来操作数据库  第一个参数 是要操作的数据库模型  第二个参数是查询的条件 pk 就相当于 表的主键 ID
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context)