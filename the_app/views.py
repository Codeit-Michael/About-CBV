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

	def post(self,request):
		my_object = PersonForm(request.POST)
		if my_object.is_valid():
			my_object.save()
			return redirect('personlist')
		return render(request,'the_app/home.html')

	def delete(self,id):
		my_object = Person.objects.get(id=id)
		my_object.delete()
		return redirect('personlist')

class PersonDetail(DetailView):
	model = Person
	context_object_name = 'person'

	def get(self,*args,**kwargs):
		print('hello world')
		return super(PersonDetail, self).get(*args,**kwargs)

	def post(self,*args,**kwargs):
		return super(PersonDetail, self).get(*args,**kwargs)

	def dispatch(self,request,*args,**kwargs):
		if self.request.POST.get('save'):
			print(self.request)
			print(True)
		return super(PersonDetail, self).dispatch(request,*args,**kwargs)

		# if request.POST.get('save'):
		# 	for item in mylist.item_set.all():
		# 		if request.POST.get(f'c{item.id}') == 'clicked':
		# 			item.is_complete = True
		# 		else:
		# 			item.is_complete = False
		# 		item.save()
		# elif request.POST.get('addItem'):
		# 	new = request.POST.get('newItem')
		# 	mylist.item_set.create(text=new, is_complete=False)
		# elif request.POST.get('delThis'):
		# 	item_index = request.POST.get('delThis')
		# 	mylist.item_set.get(id=item_index).delete()

		# return super(PersonDetail, self)
		# WORK ON GIVING BOOLEAN (UPDATEVIEW) & CREATING NEW ONE (CREATEVIEW)