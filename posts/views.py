from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView,TemplateView

from posts.forms import ArticleForm, ProfileForm
from posts.models import Article, Profile
from authapp.models import MyUser
from posts.decorators import signin_required


@method_decorator(signin_required, name="dispatch")
class CreateArticle(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'userhome.html'
    success_url = reverse_lazy('userhome')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(signin_required, name="dispatch")
class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'
    pk_url_kwarg = 'id'


@method_decorator(signin_required, name="dispatch")
class ArticleList(ListView):
    model = Article
    template_name = 'articlelist.html'
    context_object_name = 'articles'


@method_decorator(signin_required, name="dispatch")
class ArticleDetail(DetailView):
    model = Article
    template_name = 'articledetail.html'
    pk_url_kwarg = 'id'


@method_decorator(signin_required, name="dispatch")
class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'updateprofile.html'
    success_url = reverse_lazy('userhome')
    pk_url_kwarg = 'id'


@method_decorator(signin_required, name="dispatch")
class ProfileDelete(DeleteView):
    model = MyUser
    template_name = 'deleteprofile.html'
    success_url = reverse_lazy('userlist')
    pk_url_kwarg = 'id'


@method_decorator(signin_required, name="dispatch")
class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'updatearticle.html'
    success_url = reverse_lazy('myarticles')
    pk_url_kwarg = 'id'


@method_decorator(signin_required, name="dispatch")
class ArticleDelete(DeleteView):
    model = Article
    template_name = 'deletearticle.html'
    success_url = reverse_lazy('userhome')
    pk_url_kwarg = 'id'


@method_decorator(signin_required, name="dispatch")
class MyArticle(ListView):
    model = Article

    template_name = 'myarticles.html'
    context_object_name = 'my_articles'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)


class IndexView(ListView):
    model =Article
    template_name = 'index.html'
    context_object_name ='articles'
