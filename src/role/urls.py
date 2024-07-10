from role.views import RoleView,PermissionView
from django.urls import path


urlpatterns = [
    path('create-role/',RoleView.as_view(),name='role_create'),
    path('create-permission/',PermissionView.as_view(),name='permission_create'),
]