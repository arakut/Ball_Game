from django.contrib import admin

# Register your models here.
from .models import Place, Review

admin.site.register(Place)
admin.site.register(Review)