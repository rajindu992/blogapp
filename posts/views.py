from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from posts.forms import ArticleForm, ProfileForm
from posts.models import Article, Profile


class CreateArticle(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'userhome.html'
    success_url = '/posts/articlelist'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'
    pk_url_kwarg = 'id'


class ArticleList(ListView):
    model = Article
    template_name = 'articlelist.html'
    context_object_name = 'articles'


class ArticleDetail(DetailView):
    model = Article
    template_name = 'articledetail.html'
    pk_url_kwarg = 'id'


class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'updateprofile.html'
    success_url = reverse_lazy('artilelist')
    pk_url_kwarg = 'id'


class ProfileDelete(DeleteView):
    model = Profile
    template_name = 'deleteprofile.html'
    success_url = reverse_lazy('login')
    pk_url_kwarg = 'id'


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'updatearticle.html'
    success_url = reverse_lazy('articlelist')
    pk_url_kwarg = 'id'


class ArticleDelete(DeleteView):
    model = Article
    template_name = 'deletearticle.html'
    success_url = reverse_lazy('articlelist.html')
    pk_url_kwarg = 'id'


class MyArticle(ListView):
    model = Article

    template_name = 'myarticles.html'
    context_object_name = 'my_articles'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)
