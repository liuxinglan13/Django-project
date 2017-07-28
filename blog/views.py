from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
import markdown



# Create your views here.


def index(request):
    # - 表示逆序 不加则是正序
    post_list = Post.objects.all().order_by('-created_time')
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    context = {'post': post}
    return render(request, 'blog/detail.html', context)