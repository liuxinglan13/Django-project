from django.shortcuts import render, get_object_or_404 ,redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm

# Create your views here.

# 评论表单填写的视图函数
# 接受的参数 post_pk 代表 被评论的文章的post（正文）的主键 ID  由 detail.html 的表单
# <form action="{% url 'comments:post_comment' post.pk %}" method="post" class="comment-form">  这一句传入接收


def post_comment(request, post_pk):
    # request.get_full_path 这个可以查看 request对象 携带的 URL地址
    # a = request.get_full_path()
    # print('a')
    # 首先根据传入的post_pk 获取被评论的文章
    post = get_object_or_404(Post, pk=post_pk)
    # 判断request的http请求方式 POST还是GET
    if request.method == 'POST':
        # request.POST 的POST并不是我们自定义的文章详情post  是指request对象中由用户post方式提交的数据
        # 利用这些数据将CommentForm函数 实例化
        form = CommentForm(request.POST)
        # is_valid() 函数检查表单中的数据是否合法
        if form.is_valid():
            # commit=False commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            # 就是先不保存数据中数据库 将实例化以便操作
            comment = form.save(commit=False)
            # 将 评论和被评论的文章关联起来 就相当于 在 comment评论的表中 为每一条评论 设置想关联的被评论文章ID
            comment.post = post
            # 最终将评论的数据保存进数据库
            comment.save()
            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            # 我们再 blog/models.py 中的 post模型中 定义过 get_absolute_url 方法了 会返回相应post文章的url
            # 这个的作用就相当于 我们 添加了一条评论后，还是自动跳转到这个被评论文章的页面
            return redirect(post)
        else:
            # # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
            # 因此我们传了三个模板变量给 detail.html，
            # 一个是文章（Post），一个是评论列表，一个是表单 form
            # 注意这里我们用到了 post.comment_set.all() 方法，
            # 这个用法有点类似于 Post.objects.all()
            # 其作用是获取这篇 post 下的的全部评论，
            # 因为 Post 和 Comment 是 ForeignKey 关联的，
            # 因此使用 post.comment_set.all() 反向查询全部评论。
            # post.comment_set.all() 等价于 Comment.objects.filter(post=post)，即根据 comment.post 来过滤该 post(文章详情) 下的全部评论
            comment_list = post.comment_set.all()
            # 从新渲染调用detail.html 模板
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list}
            return render(request, 'blog/detail.html', context)
    return redirect(post)
