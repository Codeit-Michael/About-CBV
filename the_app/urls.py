from django.urls import path
from . import views
from .views import PersonList, PersonDetail, PersonCreate, PersonDelete, PersonUpdate

urlpatterns = [
	# path('', views.person_list, name='personlist'),
	# path('del/pk=<int:pknum>', views.delThis, name='delThis'),
	# path('pd/pk=<int:id>', views.get_id, name='getid'),
	# path('pd/pk=<int:id>', PersonList.read, name='read'),
	path('person-list', PersonList, name='personlist'),
	path('person-delete/pk=<int:pk>', PersonDelete, name='persondelete'),
	# path('del/<int:id>', PersonList.delete, name='persondelete'),
	path('person-detail/pk=<int:pk>', PersonDetail, name='persondetail'),
	# path('pd/pk=<int:pk>', PersonDetail.new_one, name='new_one'),
	# path('person-create/', PersonCreate, name='personcreate')
	path('person-create/', PersonCreate, name='personcreate'),
	path('person-update/pk=<int:pk>', PersonUpdate, name='personupdate'),
	path('signup/', views.signup, name='signup'),
	path('signin/', views.signin, name='signin'),
	path('signout/', views.signout, name='signout'),
]