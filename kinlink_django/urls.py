from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from kinlink.views import MyTokenObtainPairView, UserProfileList, UserProfileDetail, PostList, PostDetail, CommentList, CommentDetail, RelationshipList, RelationshipDetail, UserList, UserDetail, UserRelationshipList
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserList.as_view(), name="user_list"),
    path('users/<int:pk>', UserDetail.as_view(), name="user_detail"),
    path('userprofiles/', UserProfileList.as_view(), name="userprofile_list"),
    path('userprofiles/<int:pk>', UserProfileDetail.as_view(), name="userprofile_detail"),
    path('posts/', PostList.as_view(), name="post_list"),
    path('posts/<int:pk>', PostDetail.as_view(), name="post_detail"),
    path('comments/', CommentList.as_view(), name="comment_list"),
    path('comments/<int:pk>', CommentDetail.as_view(), name="comment_detail"),
    path('relationships/', RelationshipList.as_view(), name="relationship_list"),
    path('relationships/to_user=<int:to_user>/', UserRelationshipList.as_view(), name="user_relationship_list"),
    path('relationships/<int:pk>', RelationshipDetail.as_view(), name="relationship_detail"), 
]

