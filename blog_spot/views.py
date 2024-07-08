from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog_spot.models import Post
# Create your views here.
from datetime import datetime

def index(requests):
    posts = Post.objects.all()
    now = datetime.now()
    
    return render(requests, "index.html", locals()) #HttpResponse(post_list)

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def showPost(requests, slug):
    #1.查詢資料庫
    try:
        post = Post.objects.get(slug=slug) #urlencoding
    except ObjectDoesNotExist:
        return redirect('/')
    except MultipleObjectsReturned:
        return redirect('/')
    
    return render(requests, 'post.html', locals())
