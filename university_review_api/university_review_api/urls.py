from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/universities/', include('apps.universities.urls')),
    path('api/reviews/', include('apps.reviews.urls')),
]
