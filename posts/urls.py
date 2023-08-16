from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostListView.as_view()),
    path('<int:pk>/',views.PostDetailView.as_view()),
    path('users/',views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    
]
