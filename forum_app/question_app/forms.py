from django import forms
from .models import Questions , Answers
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class QuestionForm(forms.ModelForm):
	class Meta:
		model = Questions
		exclude = ("author",)



class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answers
		fields = ('anwser', )


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		
		user.save()
		return user