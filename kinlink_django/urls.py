from django.contrib import admin
from django.urls import path, include
from kinlink import views
from kinlink.views import MyTokenObtainPairView, UserProfileList, UserProfileDetail
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('userprofiles/', UserProfileList.as_view(), name="userprofile-list"),
    path('userprofiles/<int:pk>/', UserProfileDetail.as_view(), name="userprofile-detail"),
]
