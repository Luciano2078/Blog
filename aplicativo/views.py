from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from .models import Post




class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post



