from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, reverse

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, DeleteView, View

from .models import Discuss, DiscussText

from .forms import DiscussForm


class DiscussListView(ListView):
    model = Discuss
    template_name = 'discuss_app/discuss.html'
    context_object_name = 'discuss'
    ordering = ['-edit_date']
    paginate_by = 5


class CreateDiscuss(CreateView):
    model = Discuss
    fields = ['title', 'text']
    template_name = 'discuss_app/create_discuss.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateDiscuss, self).form_valid(form)

    def get_success_url(self):
        return reverse('detail-discuss', kwargs={'pk' : self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CreateDiscuss, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs


class DiscussDetailView(DetailView):
    model = Discuss
    template_name = 'discuss_app/detail_discuss.html'
    context_object_name = 'detaildiscuss'


class DiscussDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Discuss
    template_name = 'discuss_app/delete_discuss.html'

    def test_func(self):
        discuss = self.get_object()
        if self.request.user == discuss.author:
            return True
        return False

    def get_success_url(self):
        messages.warning(self.request, f'Ваше обсуждение успешно удалено.')
        return reverse("discuss-list")


class AddTextDiscuss(View):
    def post(self, request, pk):
        form = DiscussForm(request.POST)
        discuss = Discuss.objects.get(id=pk)
        user = request.user
        if form.is_valid():
            form = form.save(commit=False)
            form.discuss = discuss
            form.author = user
            form.save()
        return redirect(discuss.get_absolute_url())
