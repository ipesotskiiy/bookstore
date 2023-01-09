from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt import views
from user.views import (
    RegisterUserAPIView,
    MyTokenObtainPairView,
    GetProfileView,
    UpdateUserView,
    # UploadViewSet,
    UploadAvatarView
)

app_name = 'user'

# router = routers.DefaultRouter()
#
# router.register(r'user/upload-avatar', UploadViewSet, basename='upload')

urlpatterns = [
    path('auth/signup', RegisterUserAPIView.as_view(), name='signup'),
    path('auth/signin', MyTokenObtainPairView.as_view(), name='signin'),
    path('auth/check-token', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/me', GetProfileView.as_view(), name='me'),
    path('user/upload-avatar', UploadAvatarView.as_view(), name='upload_avatar'),
    path('user/<pk>', UpdateUserView.as_view(), name='update_user')
]
