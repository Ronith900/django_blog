from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import UserRegisterForm, UserProfileForm
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class RegisterUser(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse('login')

    def form_valid(self, form):
        user_object = form.save()
        messages.success(self.request, f'Account created for {user_object.username}!')
        return HttpResponseRedirect(self.get_success_url())


class UserProfile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'


class UserProfileEdit(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'users/profile_edit.html'


    def get_success_url(self):
        return reverse('user-profile',kwargs={'pk': self.object.user.pk})