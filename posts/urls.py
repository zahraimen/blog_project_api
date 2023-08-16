from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet,UserViewSet

router =SimpleRouter()
router.register('users',UserViewSet,basename='users')
router.register('',PostViewSet,basename='posts')

urlpatterns = router.urls





# urlpatterns = [
#     path('',PostListView.as_view()),
#     path('<int:pk>/',PostDetailView.as_view()),
#     path('users/',UserListView.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
    
# ]
