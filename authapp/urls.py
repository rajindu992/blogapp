from django.urls import path

from authapp import views

urlpatterns=[
    path('signup',views.SignUp.as_view(),name='signup')
]