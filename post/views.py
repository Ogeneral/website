from django.template import RequestContext, loader
from post.models import Post
from post.models import Comment
from post.forms import PostForm, CommentForm
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
    return render_to_response('index3.html',  context={"latest_post_list":latest_post_list})
      # (request, {'latest_post_list': latest_post_list}))




def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('http://localhost:8000/posts/')
    return render(template_name = 'add_post.html',
                  context={"form":form},
                  request = request)
 

def detail(request, post_id):
  p = Post.objects.get(pk=post_id)
  form = CommentForm(request.POST or None)
  if form.is_valid():
        comment = form.save(commit=False)
        comment.save()
        return redirect('http://localhost:8000/posts/')
  p = Post.objects.get(pk=post_id)
  return render_to_response('detail3.html', context={'post': p, 'form':form})



def add_comment(request, post_id):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.save()
        return redirect('http://localhost:8000/posts/')
    return render(template_name = 'detail3.html',
                  context={"form":form},
           
                  request = request)
