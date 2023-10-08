from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogPostForm, CommentForm
from .models import BlogPost, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('blog_post_details', pk=new_post.pk)
    else:
        form = BlogPostForm()
    return render(request,'blog/blog_post_creation.html', context={'form':form})


def update_blog_post(request,pk):
    blog_post = get_object_or_404(BlogPost,pk=pk)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog_post)
        if form.is_valid():
            edited_post = form.save()
            return redirect('blog_post_details', pk=edited_post.pk)
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, "blog/update_post_page.html", context={'form':form,'pk':pk})

def delete_blog_post(request, pk):
    blog_post = get_object_or_404(BlogPost,pk=pk)
    if request.method == 'POST':
        blog_post.delete()
        return redirect('index')
    return render(request,'blog/delete_post_page.html', {'blog_post':blog_post})

def blog_post_details(request, pk):
    blog_post = get_object_or_404(BlogPost,pk=pk)
    comments =  blog_post.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = blog_post
            comment.author = request.user
            comment.save()
            return HttpResponseRedirect(reverse('blog_post_details', args=[str(pk)]))
    else:
        form = CommentForm()
    return render(request, 'blog/blog_post_details.html', {'blog_post':blog_post,'comments':comments,'form':form})


def like_post(request, pk):
    blog_post = get_object_or_404(BlogPost,pk=pk)
    user = request.user
    if user in blog_post.likes.all():
        blog_post.likes.remove(user)
    else:
        blog_post.likes.add(user)
    return HttpResponseRedirect(reverse('blog_post_details', args=[str(pk)]))

def comments(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = post.comments.all()
    