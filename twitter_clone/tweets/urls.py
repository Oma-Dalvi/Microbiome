from django.urls import path
from .views import TweetListCreateView, LikeCreateView, CommentCreateView, ShareCreateView

urlpatterns = [
    path('tweets/', TweetListCreateView.as_view(), name='tweet-list-create'),
    path('like/', LikeCreateView.as_view(), name='like-create'),
    path('comment/', CommentCreateView.as_view(), name='comment-create'),
    path('share/', ShareCreateView.as_view(), name='share-create'),
]
