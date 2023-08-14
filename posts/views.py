
from rest_framework import generics,permissions

from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostListView(generics.ListCreateAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer