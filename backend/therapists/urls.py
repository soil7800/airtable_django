from django.urls import path

from .views import TherapistList, TherapistDetail, MethodDetail


urlpatterns = [
    path('therapist/', TherapistList.as_view(), name='therapist-list'),
    path('therapist/<slug:pk>/', TherapistDetail.as_view(), name='therapist-detail'),
    path('method/<slug:pk>/', MethodDetail.as_view(), name='method-detail')
    
]