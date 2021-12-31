from django.forms import ModelForm
from .models import Person, Task

class PersonForm(ModelForm):
	class Meta:
		model = Person
		fields = '__all__'


class PersonUpdateForm(ModelForm):
	class Meta:
		model = Person
		fields = ['name']