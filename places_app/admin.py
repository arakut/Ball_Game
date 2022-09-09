from django.contrib import admin

# Register your models here.
from .models import Place, Raiting, RaitingPLace, Review

admin.site.register(Place)
admin.site.register(Raiting)
admin.site.register(RaitingPLace)
admin.site.register(Review)