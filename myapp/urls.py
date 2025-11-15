from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
#path('posts/create/', views.post_create_form, name='post_create_form'),
    path('posts/create_modelform/', views.post_create_modelform, name='post_create_modelform'),
]
