from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person
from django.views.generic import View

# Create your views here.
# class PersonList(View):
# 	def get(self,request):
# 		people = Person.objects.all()
# 		context = {'person_list':people}
# 		return render(request, 'the_app/home.html', context)

# 	def post(self,request):
# 		pass

def persons(request):
	person_list = Person.objects.all()
	my_form = PersonForm()
	if request.method == 'POST':
		my_form = PersonForm(request.POST)
		if my_form.is_valid():
			my_form.save()
			return redirect('persons')
	context = {"person_list":person_list,"my_form":my_form}
	return render(request, 'the_app/home.html', context)