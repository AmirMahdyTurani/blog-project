from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index-page'),
    path('posts', posts, name='posts-age'),
    path('posts/<slug:slug>', post, name='post-detail-page'),
]
