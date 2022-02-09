from django.urls import path

from posts import views

urlpatterns =[
    path('createarticle',views.CreateArticle.as_view(),name='createarticle'),
    path('profile/<int:id>',views.ProfileView.as_view(),name='profile'),
    path('articlelist',views.ArticleList.as_view(),name='userhome'),
    path('articledetail/<int:id>',views.ArticleDetail.as_view(),name='articledetail'),
    path('updateprofile/<int:id>',views.ProfileUpdate.as_view(),name='updateprofile'),
    path('deleteprofile/<int:id>',views.ProfileDelete.as_view(),name='deleteprofile'),
    path('updatearticle/<int:id>',views.ArticleUpdate.as_view(),name='updatearticle'),
    path('deletearticle/<int:id>',views.ArticleDelete.as_view(),name='deletearticle'),
    path('myarticles',views.MyArticle.as_view(),name='myarticles'),
    path('index',views.IndexView.as_view(),name='index')

]