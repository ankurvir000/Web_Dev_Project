from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post



def home(request):

    return render(request,"firstweb/home.html", {'posts':Post.objects.all(), 'title':'Home'})

def index(request):
    return render(request,'firstweb/index.html', {'posts':Post.objects.all(), 'title':'Home'})

class PostListView(ListView): # <app>/<model>_<view_type>.html -> naming convention for list view 
    model = Post
    template_name = 'firstweb/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView): # <app>/<model>_<view_type>.html -> naming convention for list view 
    model = Post
    template_name = 'firstweb/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostdetailView(DetailView):# <app>/<model>_<view_type>.html -> naming convention for list view 
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView): # for create and update view it will look for <app>/<model>_form.html
    model = Post
    fields = ['title','content','image']

    def form_valid(self,form):
        form.instance.author = self.request.user

        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):# for create and update view it will look for <app>/<model>_form.html
    model = Post
    fields = ['title','content','image']

    def form_valid(self,form):
        form.instance.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):# <app>/<model>_confirm_delete.html
    model = Post
    success_url = "/"
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request,"firstweb/about.html", {'title':'About'})

def contact(request):
    return HttpResponse("<h1> Contact </h1>")