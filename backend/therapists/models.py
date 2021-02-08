from django.db import models
from django.utils import timezone


class Therapist(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=255, unique=True)
    name = models.CharField(max_length=255)
    photo_url = models.URLField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    method = models.ManyToManyField(to='Method', blank=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Method(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class RawAirtableData(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    airtable_data = models.JSONField()