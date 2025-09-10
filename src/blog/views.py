from django.shortcuts import render
from datetime import date
from django.shortcuts import get_object_or_404
from . import models



def starting_page(request):
    posts = models.Post.objects.all().order_by("-date")[0:3]
    return render(request,'blog/index.html',{
        "posts":posts,
    })


def posts(request):
    posts = models.Post.objects.all()
    return render(request,'blog/all-posts.html',{
        "posts":posts,
    })

def post_detail(request,slug):
    post = get_object_or_404(models.Post,slug=slug)
    return render(request,'blog/post-detail.html',{
        "post":post,
    })