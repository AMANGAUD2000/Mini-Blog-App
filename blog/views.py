from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import datetime
from .forms import *
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.


def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'blog/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'blog/home.html')


def blogs_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/bloglist.html', {'posts': posts})


def blogger_detail(request, author_id):
    return render(request, 'blog/base.html')


def blog_post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def bloggers_list(request):
    return render(request, 'blog/base.html')
