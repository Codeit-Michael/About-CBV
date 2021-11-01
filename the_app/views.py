from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
## Listview: show objects
class PersonList(ListView):
	model = Person
	template_name = 'the_app/home.html'
	context_object_name = 'person_list'

## Detailview: show details of each object
class PersonDetail(DetailView):
	model = Person
	context_object_name = 'person'

## CreateView: making an object
# class PersonCreate(CreateView):
# 	model = Person
# 	fields = '__all__'
# 	# reverse_lazy: almost the same as redirect
# 	success_url = reverse_lazy('personlist')

class PersonCreate(CreateView):
	template_name = 'the_app/person_form.html'
	form_class = PersonForm
	success_url = reverse_lazy('personlist')

	def save_it(self,form):
		newPeeps = form.save()
		return super(PersonCreate, self).form_valid(form)

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