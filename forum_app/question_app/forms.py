from django import forms
from .models import Questions , Answers



class QuestionForm(forms.ModelForm):
	class Meta:
		model = Questions
		exclude = ("author",)

