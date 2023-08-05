from django.contrib import admin
from django.urls import path
from .views import list_questions



urlpatterns = [
    path('', list_questions ),
]

