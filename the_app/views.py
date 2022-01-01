from django.shortcuts import render,redirect
from .forms import PersonForm, PersonUpdateForm, CreateUserForm
from .models import Person, Task
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticated_user

# Create your views here.
@login_required(login_url='signin')
class PersonList(View):

	def get(self,request):
		people = Person.objects.all()
		context = {'person_list':people}
		return render(request,'the_app/home.html',context)


@login_required(login_url='signin')
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


@login_required(login_url='signin')
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


@login_required(login_url='signin')
class PersonDelete(DeleteView):
	model = Person
	# default template_name "person_confirm_delete.html"
	success_url = reverse_lazy('personlist')


@login_required(login_url='signin')
class PersonUpdate(UpdateView):
	model = Person
	fields = ['name']
	template_name_suffix = '_update_form'
	success_url = reverse_lazy('personlist')


@unauthenticated_user
def signup(request):
	user_form = CreateUserForm()

	if request.method == 'POST':
		user_form = CreateUserForm(request.POST)

		if user_form.is_valid:
			user_form.save()
			user_name = user_form.cleaned_data.get('username')
			messages.success(request,f'user {user_name} created successfully!!')
			return redirect('signin')
		
		else:
			messages.error(request,f'Action denied, pls try again...')
			return redirect('signup')

	context = {'form':user_form}
	return render(request,'the_app/signup.html',context)



@unauthenticated_user
def signin(request):
	if request.method == 'POST':
		my_name = request.POST.get('username')
		my_pass = request.POST.get('pass')
		user = authenticate(request,username='my_name',password='my_pass')

		if user is not None:
			print(True)
			login(request,user)
			print(False)
			return redirect('personlist')

		else:
			messages.error(request,'BOBO AMP')
			return redirect('signin')

	return render(request,'the_app/signin.html')


@unauthenticated_user
def signout(request):
	logout(request)
	messages.success(request,'User successfully logged out')
	return redirect('signin')


# try it later with signin, signup and signout
class PersonAuth(View):
	pass