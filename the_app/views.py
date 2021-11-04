from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
class PersonList(View):
	def get(self,request):
		myForm = PersonForm()		
		people = Person.objects.all()
		context = {'person_list':people,'myForm':myForm}
		return render(request, 'the_app/home.html', context)

	def post(self,request):
		my_object = PersonForm(request.POST)
		if my_object.is_valid():
			my_object.save()
			return redirect('personlist')
		return render(request, 'the_app/home.html', context)

	def delete(self,request,id):
		my_object = Person.objects.get(id=id)
		print(my_object)
		return redirect('personlist')


# def person_list(request):
# 	people = Person.objects.all()
# 	myForm = PersonForm()
# 	if request.method == 'POST':
# 		my_object = PersonForm(request.POST)
# 		if my_object.is_valid():
# 			my_object.save()
# 			return redirect('personlist')
# 	context = {'person_list':people,'myForm':myForm}
# 	return render(request, 'the_app/home.html', context)

# def delThis(request,id):
# 	people = Person.objects.get(id=id)
# 	print(people)
# 	return redirect('personlist')