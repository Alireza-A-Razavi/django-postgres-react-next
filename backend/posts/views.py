from django.shortcuts import render
from rest_framework import viewsets,

from .models import Post
from .serializers import PostSerializer

class PostModelViewSet(viewsets.ModelViewSet):
	serializer_class = PostSerializer
	queryset = Post.objects.all()
