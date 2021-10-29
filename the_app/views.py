from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
class PersonList(ListView):
	model = Person
	template_name = 'the_app/home.html'
	context_object_name = 'person_list'

class PersonDetail(DetailView):
	model = Person
	context_object_name = 'person'


# class PersonList(View):
# 	def get(self,request):
# 		people = Person.objects.all()
# 		context = {'person_list':people}
# 		return render(request, 'the_app/home.html', context)

# 	def post(self,request):
# 		pass

# def personList(request):
# 	person_list = Person.objects.all()
# 	my_form = PersonForm()
# 	if request.method == 'POST':
# 		my_form = PersonForm(request.POST)
# 		if my_form.is_valid():
# 			my_form.save()
# 			return redirect('persons')
# 	context = {"person_list":person_list,"my_form":my_form}
# 	return render(request, 'the_app/home.html', context)