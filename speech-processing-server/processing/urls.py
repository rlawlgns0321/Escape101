from django.urls import path
from . import views

urlpatterns = [
    path('', views.speech_processing),
]
