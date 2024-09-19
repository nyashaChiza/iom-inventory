from django.urls import path
from .views import UserListView, UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_index'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]