from django.contrib import admin
from .models import Patient
from .models import Staff

admin.site.register(Patient)
admin.site.register(Staff)