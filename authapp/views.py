from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login

from authapp.admin import UserCreationForm
from authapp.models import MyUser
from posts.models import Profile


class SignUp(CreateView):
    model = MyUser
    form_class = UserCreationForm
    template_name = 'signup.html'

    def form_valid(self,form):
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            profile, created = Profile.objects.get_or_create(user=user)
            login(self.request, user)
            if request.user.is_authenticated:
                return redirect('posts/articlelist')



def loghome(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admins/adminhome')
        else:
            return redirect('posts/articlelist')

    return redirect('posts/index')
