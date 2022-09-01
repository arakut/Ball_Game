from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from cards_core.models import Playground
import folium
# Create your views here.

class ListObjectsView(ListView):
    model = Playground
    template_name = 'main.html'
    context_object_name = 'playgrounds'

class DetailObectView(DetailView):
    model = Playground
    template_name = 'detail.html'
    context_object_name = 'detail'

class PlaygroundCreateView(CreateView):
    model = Playground
    fields = ['adress', 'city', 'kind_sport', 'type_pg', 'coating', 'avrg_capacity', 'image', 'descr']
    success_url = '/'
    template_name = 'create_pg.html'

class PGUpdateView(UpdateView):
    model = Playground
    template_name = 'edit_pg.html'
    fields = 'adress', 'city', 'kind_sport', 'type_pg', 'coating', 'avrg_capacity', 'image', 'descr'
    success_url = '/'

class PGDeleteView(DeleteView):
    model = Playground
    success_url = '/'
    template_name = 'ymaps.html'

