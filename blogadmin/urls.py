from django.urls import path

from blogadmin import views


urlpatterns = [
    path('signin', views.SignIn.as_view(), name='signin'),
    path('adminhome',views.AdminHome.as_view(),name='adminhome'),
    path('userlist',views.UserList.as_view(),name='userlist'),
    path('userposts',views.UserPosts.as_view(),name='userposts'),
    path('postdetail/<int:id>',views.PostDetail.as_view(),name='postdetail'),

    path('search/', views.UserSearch.as_view(), name='profile-search'),
    path('searchpost',views.PostSearch.as_view(),name='postsearch')

]