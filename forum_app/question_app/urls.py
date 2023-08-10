from django.contrib import admin
from django.urls import path
from .views import list_questions , add_question , question_details , update_question , question_delete , register , login_user , logout_user



urlpatterns = [
    path('list_questions', list_questions , name="home" ),
    path('add_question' , add_question , name="add_question" ),
    path('question_details/<int:q_id>' , question_details , name='question_details'),
    path('update_question/<int:q_id>' , update_question , name='update_question'),
    path('question_delete/<int:q_id>' , question_delete , name='question_delete'),
    path('register' , register , name='register'),
    path('' , login_user , name='login_user'),
    path('logout_user' , logout_user , name='logout_user')
    


]

