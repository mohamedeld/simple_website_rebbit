from django.shortcuts import render
from post.serializers import PostSerializer
from rest_framework import generics,permissions
# Create your views here.
from .models import Post
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    
    def perform_create(self,serializer):
        serializer.save(poster= self.request.user)
        