from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate

from authapp.admin import UserCreationForm
from authapp.models import MyUser
from posts.models import Profile


# class SignUp(CreateView):
#     model = MyUser
#     form_class = UserCreationForm
#     template_name = 'signup.html'
#     success_url = reverse_lazy('userhome')
# 
#     def form_valid(self, form):
#         if form.is_valid():
#             user = form.save()
#             user.set_password(user.password)
#             profile, created = Profile.objects.get_or_create(user=user)
# 
#             login(self.request, user)
#             return redirect('userhome')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile, created = Profile.objects.get_or_create(user=user)

            user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.email, password=raw_password)
            login(request, user)
            return redirect('userhome')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def loghome(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admins/adminhome')
        else:
            return redirect('posts/articlelist')

    return redirect('posts/index')
