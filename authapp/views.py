
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authapp.admin import UserCreationForm
from authapp.models import MyUser
from posts.models import Profile


class SignUp(CreateView):
    model = MyUser
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            profile, created = Profile.objects.get_or_create(user=user)

        return super(SignUp, self).form_valid(form)


def loghome(request):
    if request.user.is_authenticated:
        return redirect('posts/articlelist')

    return render(request, 'registration/loghome.html')
