from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Questions(models.Model):

	author = models.ForeignKey(User , on_delete=models.SET_NULL,null=True , blank=True , related_name="quetion_user")
	content= models.TextField(max_length=200)
	tags = TaggableManager(blank=True)
	question= models.CharField(max_length=100)
	create_at = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.question

	def get_tags(self):
		my_tag = []
		for tag in self.tags.all():
			my_tag.append(str(tag))
		return ', '.join(my_tag)


class Answers(models.Model):

	anwser= models.TextField(max_length=200)
	Quetion = models.ForeignKey(Questions , on_delete= models.CASCADE, related_name="answer_question")
	create_at = models.DateTimeField(default= timezone.now())
	author = models.ForeignKey(User , on_delete=models.SET_NULL,null=True , blank=True , related_name="answer_user")

	def __str__(self):
		return self.author



