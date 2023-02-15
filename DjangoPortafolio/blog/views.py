from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.



def posts(request):
    posts=Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def post_detail(request, post_id):
    posts=get_object_or_404(Post, pk=post_id )
    return render(request, 'post_detail.html', {'posts': posts})    