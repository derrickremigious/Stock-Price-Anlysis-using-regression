from django.contrib import admin

# Register your models here.
from .models import Tcs,Accenture

admin.site.register(Accenture)
admin.site.register(Tcs)