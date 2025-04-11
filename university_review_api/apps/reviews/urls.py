from django.urls import path
from .views import ReviewCreateView, ReviewDetailView, ReviewSearchView

urlpatterns = [
    path('', ReviewCreateView.as_view(), name='review-create'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('search/', ReviewSearchView.as_view(), name='review-search'),
]