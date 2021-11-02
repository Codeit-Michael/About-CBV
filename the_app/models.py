from django.db import models

# # Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Task(models.Model):
	peep = models.ForeignKey(Person, on_delete=models.CASCADE)
	task = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.task