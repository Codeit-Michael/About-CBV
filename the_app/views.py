from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person, Task
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
class PersonList(View):

	def get(self,request):
		people = Person.objects.all()
		context = {'person_list':people}
		return render(request,'the_app/home.html',context)


class PersonDetail(DetailView):
	model = Person
	context_object_name = 'person'

	def get(self,*args,**kwargs):
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


class PersonCreate(View):

	def get(self,request):
		my_form = PersonForm()
		return render(request,'the_app/person_form.html',{'form':my_form})

	def post(self,request):
		my_form = PersonForm(request.POST)
		if my_form.is_valid():
			my_form.save()
			my_name = my_form.cleaned_data.get('name')
			my_object = Person.objects.get(name=my_name).id
			return redirect('persondetail',my_object)
		return render(request,'the_app/person_form.html',{'form':my_form})


class PersonDelete(DeleteView):
	model = Person
	# default template_name "person_confirm_delete.html"
	success_url = reverse_lazy('personlist')


class PersonUpdate(UpdateView):
	model = Task
	fields = ['is_complete']
	template_name_suffix = '_update_form'
	success_url = reverse_lazy('personlist')


"""
~ WE ONLY GET 1 TASK ON THE PERSON OBJECT THAT'S WHY WE ONLY HAVE 1 FORM 
FOR IT. I WNAT YOU TO GIVE FORM TO ALL OF THE OBJECT'S 'is_complete' ATTR.
"""