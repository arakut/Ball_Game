from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.views.generic import DetailView

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users_app/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':

        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if p_form.is_valid():

            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')

    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }
    return render(request, 'users_app/profile.html', context)


class UserProfile(DetailView):
    model = Profile
    template_name = 'users_app/user_profile.html'
    context_object_name = 'profile'

