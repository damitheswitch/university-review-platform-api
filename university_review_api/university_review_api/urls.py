from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('university_review_api.apps.users.urls')),
    path('api/universities/', include('university_review_api.apps.universities.urls')),
    path('api/reviews/', include('university_review_api.apps.reviews.urls')),
    path('api/users/', include('university_review_api.apps.users.urls_profile')),
]