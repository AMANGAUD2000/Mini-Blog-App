from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('home/', views.home, name="home"),
    path('blogs/', views.blogs_list, name="blogs_list"),
    path('bloggers/', views.bloggers_list, name="bloggers_list"),
    path('blogger/<str:author_id>', views.blogger_detail, name="blogger_detail"),
    path('blogs/<str:pk>/', views.blog_post_detail, name="blog_post_detail"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
]
