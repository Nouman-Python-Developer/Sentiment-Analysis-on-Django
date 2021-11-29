
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('decision_app/', views.MainPageView.as_view(), name='main-page'),
]
