from django.urls import path
from apps.users.views import RegisterView, LoginView, UserProfileView, UserReviewsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('reviews/', UserReviewsView.as_view(), name='user-reviews'),
]
