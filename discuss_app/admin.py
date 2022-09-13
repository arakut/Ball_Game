from django.contrib import admin

# Register your models here.
from .models import Discuss, DiscussText

admin.site.register(Discuss)
admin.site.register(DiscussText)