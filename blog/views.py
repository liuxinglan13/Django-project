from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
import markdown
from comments.forms import CommentForm
from django.views.generic import ListView, DetailView


# Create your views here.

# 类视图函数


class IndexView(ListView):
    # 将 model 指定为 Post，告诉 Django 我要获取的模型是 Post。
    model = Post
    # 指定这个视图渲染的模板
    template_name = 'blog/index.html'
    # 指定获取的模型列表数据保存的变量名。这个变量会被传递给模板。post_list 会被传递给html模板 用来填充数据 其中包含了 Post模型的相应数据
    context_object_name = 'post_list'
    # 类视图 ListView 自带分页功能
    # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 5

# 函数试图    上下两者作用是一样的
'''
def index(request):
    # - 表示逆序 不加则是正序
    post_list = Post.objects.all()[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)
'''


# 用类试图 重新 detail函数


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super(PostDetailView, self).get(request, *args, **kwargs)

        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()

        # 视图必须返回一个 HttpResponse 对象
        return response

    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post = super(PostDetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return post

    def get_context_data(self, **kwargs):
        # 覆写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
        # 还要把评论表单、post 下的评论列表传递给模板。
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context


'''
# 函数视图  detail
def detail(request, pk):
    # get_object_or_404 用来操作数据库  第一个参数 是要操作的数据库模型  第二个参数是查询的条件 pk 就相当于 表的主键 ID
    post = get_object_or_404(Post, pk=pk)

    # 每当detail文章详情函数被调用 说明文章被人阅读了 就调用 方法使阅读量+1
    post.increase_views()
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    # 实例化表单
    form = CommentForm()
    # 获取该片文章下所有的评论列表
    comment_list = post.comment_set.all()
    # # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context)
'''