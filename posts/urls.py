from django.urls import path
from .views import PostListView,PostDetailView,UserListView,UserDetail

urlpatterns = [
    path('',PostListView.as_view()),
    path('<int:pk>/',PostDetailView.as_view()),
    path('users/',UserListView.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    
]
