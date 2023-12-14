# tweets/views.py

from rest_framework import generics
from .models import Tweet, Like, Comment, Share
from .serializers import TweetSerializer, LikeSerializer, CommentSerializer, ShareSerializer


class TweetListCreateView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ShareCreateView(generics.CreateAPIView):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer
