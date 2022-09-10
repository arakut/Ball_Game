from django.db.models import Q

from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import View

from .models import Place, Review
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

from .forms import ReviewForm

def about(request):
    return render(request, 'places_app/about.html', {})

def contacts(request):
    return render(request, 'places_app/contacts.html', {})


class PlaceListView(ListView):
    model = Place
    template_name = 'places_app/home.html'
    context_object_name = 'places'
    ordering = ['-edit_date']
    paginate_by = 5


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'places_app/detail.html'
    context_object_name = 'place1'


class PlaceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Place
    fields = ['image', 'city', 'open_hours', 'close_hours', 'type_pg', 'coating', 'descr']
    template_name = 'places_app/update_place.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Ваш изменения успешно внесены.')
        return super().form_valid(form)

    def test_func(self):
        place = self.get_object()
        if self.request.user == place.author:
            return True
        return False

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("detail", kwargs={"pk": pk})


class PlaceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Place
    template_name = 'places_app/confirm_delete.html'

    def test_func(self):
        place = self.get_object()
        if self.request.user == place.author:
            return True
        return False

    def get_success_url(self):
        messages.warning(self.request, f'Ваша площадка успешно удалена.')
        return reverse("home")

class PlaceCreateView(CreateView):
    model = Place
    fields = ['city', 'image', 'adress', 'kind_sport', 'open_hours', 'close_hours', 'type_pg', 'coating', 'descr']
    template_name = 'places_app/new_place.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Ваша площадка успешно добавлена.')
        return super(PlaceCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('detail', kwargs={'pk' : self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(PlaceCreateView, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs


class SearchPlacesView(ListView):
    model = Place
    template_name = 'places_app/search.html'
    context_object_name = 'places'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Place.objects.filter(Q(adress__icontains=query)|Q(descr__icontains=query)|Q(kind_sport__icontains=query)|Q(city__icontains=query))
        return object_list


# TODO доделать отображение всех комментариев на странице
class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        place = Place.objects.get(id=pk)
        user = request.user
        if form.is_valid():
            form = form.save(commit=False)
            form.place = place
            form.author = user
            form.save()
        return redirect(place.get_absolute_url())

