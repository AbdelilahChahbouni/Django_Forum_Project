from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions , Answers




def list_questions(request):
    d = Questions.objects.all().values()
    #data = Questions.tags.all()
    data2 = Questions.tags.values_list('name' , flat=True)
    new_data = zip(d , data2)
    



    return render(request,"list_questions.html" , {'que' : d , 'new_data': new_data})

    


    

