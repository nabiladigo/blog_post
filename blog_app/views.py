from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post 

# Create your views here.

def home(request):
    return render(request, "home.html", {})

class Post(ListView):
    model= Post
    template_name= "posts/post.html"
