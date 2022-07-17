"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('intro/', views.IntroView.as_view(),name='intro'),
    path('admin/', views.AdminView.as_view(),name='admin'),
    path('login/', views.LoginView.as_view(),name='login'),
    path('logout/', views.LogoutView.as_view(),name='logout'),
    path('loginfail/', views.LoginFailView.as_view(),name='loginfail'),
    path('sigungu/', views.SigunguView.as_view(),name='sigungu'),
    path('mypage/', views.MypageView.as_view(),name='mypage'),
    path('mypageup/', views.MypageupView.as_view(),name='mypageup')

]
