from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Therapist, Method


class MethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Method
        fields = ['url', 'id', 'title']


class TherapistSerializer(serializers.HyperlinkedModelSerializer):
    method = MethodSerializer(many=True, read_only=True)

    class Meta:
        model = Therapist
        fields = ['url', 'id', 'name', 'photo_url', 'method']