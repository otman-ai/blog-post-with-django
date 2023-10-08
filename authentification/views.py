from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, LoginForm
from blogs.models import BlogPost

def index(request):
    blog_posts = BlogPost.objects.all()
    return render(request,'index.html',context={"blog_posts": blog_posts})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "registration/signup.html",{"form":form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,password=password)
            if user:
                print("Login successfully")
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, "registration/login.html",{'form':form})

def user_logout(request):
    logout(request)
    return redirect("login")
            
