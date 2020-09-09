from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views import generic
from .models import *
from . import forms
# Create your views here.
def home(request):
    post = Post.objects.all()[::-1]
    context = {'post':post}
    return render(request,'my_app/home.html',context)

def sign_in(request):
    form = forms.CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:login')
    return redirect(request,'my_app/post_form.html',{'form':form})



class NewPost(generic.CreateView):

    form_class = forms.CreatePost
    template_name = 'my_app/post_form.html'



# def create_post(request,*kwargs):
#     form = forms.CreatePost()
#     if request.method == 'POST':
#         form = forms.CreatePost(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('my_app:post_detail', kwargs={'pk':request.post.pk})
#
#     return render(request,'my_app/post_form.html',{'form':form})

def post_detail(request,pk):
    post = Post.objects.get(id=pk)
    return render(request,'my_app/post_detail.html',{'post':post})

def post_delete(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('my_app:home')

def post_update(request,pk):
    post = Post.objects.get(id=pk)
    form = forms.CreatePost(instance=post)

    if request.method == 'POST':
        form = forms.CreatePost(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('my_app:post_detail', pk=post.pk)
    return render(request,'my_app/post_form.html',{'form':form,'post':post})


def post_publish(request,pk):
    post = get_object_or_404(Post,id=pk)
    post.publish()
    return redirect('my_app:post_detail', pk=post.pk)

def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)

    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('my_app:post_detail',pk=post.pk)
    else:
        form = forms.CommentForm()
    return render(request,'my_app/post_form.html',{'form':form})

def comment_approve(request,pk):
    comment = get_object_or_404(Comments,id=pk)
    comment.approved()
    return redirect('my_app:post_detail', pk=comment.post.pk)

def comment_remove(request,pk):
    comment = get_object_or_404(Comments,id=pk)
    comment.delete()
    post_pk = comment.post.pk
    return redirect('my_app:post_detail', pk=post_pk)


def draftlist(request):
    post = Post.objects.filter(published__isnull=True).order_by('created')
    return render(request,'my_app/draftlist.html',{'post':post})
