from django.forms import ModelForm
from .models import Person, Task

class PersonForm(ModelForm):
	class Meta:
		model = Person
		fields = '__all__'


class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['is_complete']