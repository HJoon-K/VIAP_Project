"""
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import path
from . import views

urlpatterns = [
    path('admin_member/', views.Admin_memberView.as_view(), name='admin_member'),
    path('admin_question/', views.Admin_questionView.as_view(), name='admin_question'),
    path('admin_reivew/', views.Admin_reviewView.as_view(), name='admin_review'),



]
