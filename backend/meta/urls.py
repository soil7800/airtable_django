from django.urls import path, include

from therapists import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v0/', include('therapists.urls')),
]
