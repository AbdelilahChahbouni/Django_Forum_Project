from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Questions , Answers
from .forms import QuestionForm




def list_questions(request):
    d = Questions.objects.all().values()
    #data = Questions.tags.all()
    data2 = Questions.tags.values_list('name' , flat=True)
    new_data = zip(d , data2)

    return render(request,"list_questions.html" , {'que' : d , 'new_data': new_data , 'data2': data2})

    
def add_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST , request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()
            return redirect("home")
    else:
        form = QuestionForm()
    return render(request , "add_question.html" , {'form':form})


def question_details(request , q_id):
    question = Questions.objects.filter(pk=q_id)
    return render(request , 'question_details.html' , {'question':question})

    

