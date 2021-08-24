from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,reverse
from django.views.generic import CreateView
from .forms import UserRegisterForm


class RegisterUser(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse('login')

    def form_valid(self, form):
        user_object = form.save()
        messages.success(self.request, f'Account created for {user_object.username}!')
        return HttpResponseRedirect(self.get_success_url())
