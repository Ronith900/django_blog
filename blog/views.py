from django.shortcuts import reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tweet
from .forms import CreateTweetForm

# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tweets'] = Tweet.objects.filter(user=self.request.user)
        return context


class About(LoginRequiredMixin, TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Page'
        return context


class Create(LoginRequiredMixin, CreateView):
    template_name = 'blog/create.html'
    form_class = CreateTweetForm

    def get_success_url(self):
        return reverse('blog-home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        context['tweet_type'] = 'Create New'
        return context


class UpdateTweet(LoginRequiredMixin, UpdateView):
    template_name = 'blog/create.html'
    form_class = CreateTweetForm
    model = Tweet

    def get_success_url(self):
        return reverse('blog-home')

    def get_context_data(self, **kwargs):
        context = super(UpdateTweet, self).get_context_data(**kwargs)
        context['tweet_type'] = 'Edit'
        return context


class DeleteTweet(LoginRequiredMixin, DeleteView):
    template_name = 'blog/Delete.html'
    model = Tweet

    def get_success_url(self):
        return reverse('blog-home')
