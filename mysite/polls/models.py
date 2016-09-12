from django.db import models

# Create your models here.
class Qestion(models.Model):
	"""docstring for Qestion"""
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	"""docstring for Choice"""
	question = models.ForeignKey(Qestion,on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)