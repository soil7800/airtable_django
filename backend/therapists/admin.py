from django.contrib import admin


from .models import Therapist, Method, RawAirtableData

admin.site.register((Therapist, Method, RawAirtableData))