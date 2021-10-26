from django.shortcuts import render
from .forms import Person_Form
from .models import Person
from django.views.generic import View

# Create your views here.
class PersonList(View):
	def get(self,request):
		people = Person.objects.all()
		context = {'people':people}
		return render(request, 'the_app/home.html', context)

	def post(self,request):
		pass