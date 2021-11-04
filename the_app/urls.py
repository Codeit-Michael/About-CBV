from django.urls import path
from . import views
from .views import PersonList#, PersonDetail, PersonCreate

urlpatterns = [
	# path('', views.person_list, name='personlist'),
	# path('del/<int:pknum>', views.delThis, name='delThis'),
	path('', PersonList.as_view(), name='personlist'),
	path('del/<int:id>', PersonList.delete, name='delThis'),
	# path('pd/pk=<int:pk>', PersonDetail.as_view(), name='persondetail'),
	# path('person-create/', PersonCreate.as_view(), name='personcreate'),
]