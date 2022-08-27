from django.shortcuts import render
from django.views.generic import ListView, DetailView
from cards_core.models import Playground
# Create your views here.

class ListObjectsView(ListView):
    model = Playground
    template_name = 'base.html'
    context_object_name = 'cards'

class DetailObjectsView(DetailView):
    model = Playground
    template_name = 'detail.html'
    context_object_name = 'card'