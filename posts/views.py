
from rest_framework import generics

from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostListView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer