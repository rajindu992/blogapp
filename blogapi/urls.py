from django.urls import path
from blogapi import views

urlpatterns = [
    path('accounts/signup',views.UserRegistrationView.as_view()),
    path('accounts/signin',views.LoginView.as_view()),
    path('accounts/logout',views.LogOut.as_view()),
    path('article/',views.ArticleCreate.as_view()),
    path('article/<int:pk>',views.ArticleDetail.as_view()),

]