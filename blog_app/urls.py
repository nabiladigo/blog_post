from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home" ),
    path('posts/', views.Post.as_view(), name="post"),
]
