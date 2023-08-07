from django.contrib import admin
from django.urls import path
from .views import list_questions , add_question , question_details



urlpatterns = [
    path('', list_questions , name="home" ),
    path('add_question' , add_question , name="add_question" ),
    path('question_details/<int:q_id>' , question_details , name='question_details')
]

