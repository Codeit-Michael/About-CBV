from django.forms import ModelForm
from .models import Person

class Person_Form(ModelForm):
	class Meta:
		model = Person
		fields = '__all__'