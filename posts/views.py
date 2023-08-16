
from django.contrib.auth import get_user_model
#from rest_framework import generics
from rest_framework import viewsets

from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer,UserSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes=(IsAuthorOrReadOnly,)
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=get_user_model().objects.all()
    serializer_class = UserSerializer
    
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=get_user_model().objects.all()
#     serializer_class=UserSerializer