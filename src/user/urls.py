from user.views import UserView
from django.urls import path

urlpatterns = [
    path('create/',UserView.as_view(),name='user_create')
]