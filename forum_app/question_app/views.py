from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Questions , Answers
from .forms import QuestionForm , AnswerForm , NewUserForm
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from taggit.models import Tag




def list_questions(request):
    d = Questions.objects.all().values()
    #data2 = Questions.tags.values_list('name' , flat=True)
    data2 = Questions.tags.all()
    new_data = zip(d , data2)
    my_loop=range(1, 8)

    return render(request,"list_questions.html" , {'que' : d , 'new_data': new_data , 'test':my_loop})

    
def add_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST , request.FILES)
        if form.is_valid():
            #new_form = form.save(commit=False)
            #new_form.author = request.user
            #new_form.save()
            form.instance.author = request.user
            form.save()
            return redirect("home")
    else:
        form = QuestionForm()
    return render(request , "add_question.html" , {'form':form})


def question_details(request , q_id):
    anwser_question = None
    question = Questions.objects.filter(pk=q_id)
    data = Questions.objects.get(pk=q_id)
    data2 = data.tags.all()
    new_tags = [tag.name for tag in data2]
    anwser_question = Answers.objects.filter(Quetion=data)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.Quetion = data
            form.save()
    else:
        form = AnswerForm()

    return render(request , 'question_details.html' , {'question':question , 'tags': new_tags , 'answer_question':anwser_question , 'form': form})


    
def update_question(request , q_id):
    q = Questions.objects.get(pk=q_id)
    if request.method == "POST":
        form = QuestionForm(request.POST , request.FILES , instance=q)
        if form.is_valid():
            form.instance.author = request.user 
            form.save()
            return redirect("home")
            
    else:
        form =QuestionForm(instance=q)
    return render(request , 'update_question.html' , {'form':form})




def question_delete(request,q_id):
    data= Questions.objects.get(pk=q_id)
    data.delete()
    return redirect("home")
    


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"form":form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form":form})


def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("login_user") 

