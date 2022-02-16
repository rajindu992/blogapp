from django.urls import path

from authapp import views
from django.urls import reverse_lazy

urlpatterns=[
    path('signup',views.signup,name='signup')
]