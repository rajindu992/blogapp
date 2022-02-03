from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.http import request, HttpResponseRedirect
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from authapp.models import MyUser
from blogadmin import forms
from blogadmin.forms import LoginForm
from posts.models import Article


class SignIn(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.LoginForm()
        context = {'form': form}
        return render(request, 'signin.html', context)

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('loghome')
            else:
                messages.error(request,"Invalid credentials")
                return render(request, 'signin.html', {'form': form})


class AdminHome(TemplateView):
    template_name = 'adminhome.html'


class UserList(ListView):
    model = MyUser
    template_name = 'userlist.html'
    ordering = ['Name']

    def get_context_data(self, *args, **kwargs):
        user_posts = MyUser.objects.annotate(total_posts=Count('article')).exclude(is_admin=True)
        ATOZID = self.request.GET.get('ATOZ')
        ZTOAID = self.request.GET.get('ZTOA')

        if ATOZID:
            user_posts = MyUser.objects.annotate(total_posts=Count('article')).exclude(is_admin=True).order_by('Name')
        if ZTOAID:
            user_posts = MyUser.objects.annotate(total_posts=Count('article')).exclude(is_admin=True).order_by('-Name')
        context = super(UserList, self).get_context_data(*args, **kwargs)
        context['user_posts'] = user_posts

        return context


class UserPosts(ListView):
    model = Article
    template_name = 'userposts.html'

    def get_context_data(self, *args, **kwargs):
        posts = Article.objects.all()
        OLDID = self.request.GET.get('OLD')
        NEWID = self.request.GET.get('NEW')
        if OLDID:
            posts = Article.objects.order_by('created_on')
        if NEWID:
            posts = Article.objects.order_by('-created_on')
        context = super(UserPosts, self).get_context_data(*args, **kwargs)
        context['posts'] = posts

        return context


class PostDetail(DetailView):
    model = Article
    template_name = 'postdetail.html'
    pk_url_kwarg = 'id'


class UserSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = MyUser.objects.filter(
            Q(Name__contains=query) | Q(email__contains=query)
        ).exclude(is_admin=True)

        context = {
            'profile_list': profile_list
        }

        return render(request, 'search.html', context)


class PostSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        try:
            post_list = Article.objects.filter(
                Q(author__Name__icontains=query) | Q(title__icontains=query))

        except:
            messages.error(request, "No posts to show")
            return render(request, 'userposts.html')

        context = {
            'post_list': post_list
        }

        return render(request, 'postsearch.html', context)
