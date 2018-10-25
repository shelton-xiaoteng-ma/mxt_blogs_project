from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post
import markdown

# Create your views here.
def index(request):
    # return HttpResponse("欢迎访问我的博客首页！")
    posts = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'post_list': posts,
    })

def detail(request, pk):
    # get_object_or_404 如果在数据库中, 则返回, 否则返回404
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, 
                                    extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',
                                    ])
    
    return render(request, 'blog/detail.html', context={'post': post})