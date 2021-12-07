from django.urls import path
from django.urls.resolvers import URLPattern
from django.views.generic.base import View

from . import views

app_name = "aplicativo"

urlpatterns = [
    path("", views.PostListView.as_view(), name='list'),
    #path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
    path("<slug:slug>/", views.post_detail, name="detail"),
]