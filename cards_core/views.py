from django.shortcuts import render
from django.views.generic import ListView, DetailView
from cards_core.models import Playground
# Create your views here.

class ListObjectsView(ListView):
    model = Playground
    template_name = 'main.html'
    context_object_name = 'playgrounds'

class DetailObectView(DetailView):
    model = Playground
    template_name = 'detail.html'
    context_object_name = 'detail'