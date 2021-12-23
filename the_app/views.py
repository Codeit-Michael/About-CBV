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
		return render(request,'the_app/home.html',context)

	def delete(self,id):
		my_object = Person.objects.get(id=id)
		my_object.delete()
		return redirect('personlist')


class PersonDetail(DetailView):
	model = Person
	context_object_name = 'person'

	def get(self,*args,**kwargs):
		if object != None:
			print(object)
		return super(PersonDetail, self).get(*args,**kwargs)

	def post(self,*args,**kwargs):
		return super(PersonDetail, self).get(*args,**kwargs)

	def dispatch(self,request,pk,*args,**kwargs):
		peep = self.model.objects.get(id=pk)
		if self.request.POST.get('save'):
			for task in peep.task_set.all():
				if request.POST.get(f't{task.id}') == 'clicked':
					task.is_complete = True
				else:
					task.is_complete = False
				task.save()
		
		elif self.request.POST.get('add_item'):
			new = request.POST.get('new_item')
			peep.task_set.create(task=new, is_complete=False)
		
		elif request.POST.get('delete_this'):
			task_index = request.POST.get('delete_this')
			peep.task_set.get(id=task_index).delete()

		return super(PersonDetail, self).dispatch(request,*args,**kwargs)


# class PersonCreate(CreateView):
# 	model = Person
# 	fields = ['name']
# 	context_object_name = 'person'
# 	success_url = reverse_lazy('personlist')
	# form_class = PersonForm
	# template_name = 'the_app/person_create.html' # matic person_form.html

	'''TRY ADDING DISPATCH()'''

	# def get_success_url(self):
		# return self.success_url

def PersonCreate(request):
	my_form = PersonForm()
	if request.method == 'POST':
		my_form = PersonForm(request.POST)
		if my_form.is_valid():
			my_form.save()
			my_name = my_form.cleaned_data.get('name')
			my_object = Person.objects.get(name=my_name)
			print(my_object.id)

	return render(request,'the_app/person_form.html',{'form':my_form})







"""
~ WORK ON GIVING BOOLEAN (UPDATEVIEW) 
~ MOVE EVERYTHING FROM VIEWS CLASS TO CREATEVIEWS CLASS (get, delete)
- OR MAKE DELETEVIEWS INSTEAD OF MAKING A FUNCTION
"""