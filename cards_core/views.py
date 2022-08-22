from django.shortcuts import render
from django.views.generic import ListView
from cards_core.models import Card
# Create your views here.

class ListObjectsView(ListView):
    model = Card
    template_name = 'base.html'
    context_object_name = 'cards'