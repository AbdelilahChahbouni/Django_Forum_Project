from django.contrib import admin
from django.urls import path
from .views import list_questions , add_question



urlpatterns = [
    path('', list_questions ),
    path('add_question' , add_question )
]

