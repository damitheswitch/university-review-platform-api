from django.urls import path
from .views import UserProfileView, UserReviewsView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('reviews/', UserReviewsView.as_view(), name='user-reviews'),
]