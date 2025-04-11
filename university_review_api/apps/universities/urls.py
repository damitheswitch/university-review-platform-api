from django.urls import path
from apps.universities.views import UniversityListView, UniversityDetailView, UniversityReviewsView

urlpatterns = [
    path('', UniversityListView.as_view(), name='university-list'),
    path('<int:pk>/', UniversityDetailView.as_view(), name='university-detail'),
    path('<int:pk>/reviews/', UniversityReviewsView.as_view(), name='university-reviews'),
]
