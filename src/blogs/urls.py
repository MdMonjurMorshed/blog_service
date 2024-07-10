from blogs.views import BlogView
from django.urls import path

urlpatterns = [
    path('create/',BlogView.as_view(),name='blog_create')
]
