from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    lookup_field = 'slug'

