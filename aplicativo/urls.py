from django.urls import path

from aplicativo import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostView.as_view(), name='index'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail' )
]