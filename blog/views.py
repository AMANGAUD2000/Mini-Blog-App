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



def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + username)

			return redirect('login')		

	context = {'form':form}
	return render(request, 'blog/register.html', context)


def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'blog/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('home')




def home(request):
    return render(request, 'blog/home.html')


def blogs_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/bloglist.html', {'posts': posts})


def blogger_detail(request, author_id):
    blogger = User.objects.get(id=author_id)
    posts = Post.objects.filter(blogger_name=author_id)
    return render(request, 'blog/bloggerdetail.html',{'blogger': blogger,'posts':posts})


def blog_post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def bloggers_list(request):
    bloggers = User.objects.all()
    return render(request, 'blog/bloggerlist.html', {'bloggers': bloggers})
