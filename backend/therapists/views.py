from rest_framework import generics

from .models import Therapist, Method
from .serializers import TherapistSerializer, MethodSerializer


class TherapistList(generics.ListAPIView):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer


class TherapistDetail(generics.RetrieveAPIView):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer


class MethodDetail(generics.RetrieveAPIView):
    queryset = Method.objects.all()
    serializer_class = MethodSerializer