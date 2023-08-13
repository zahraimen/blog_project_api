from django.urls import path
from .views import PostListView,PostDetalView

urlpatterns = [
    path('',PostListView.as_view()),
    path('<int:pk>/',PostDetalView.as_view()),
]
