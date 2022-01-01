from django.forms import ModelForm
from .models import Person, Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PersonForm(ModelForm):
	class Meta:
		model = Person
		fields = '__all__'


class PersonUpdateForm(ModelForm):
	class Meta:
		model = Person
		fields = ['name']


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','password1','password2']