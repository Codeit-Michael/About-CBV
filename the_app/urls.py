from django.urls import path
from . import views
from .views import PersonList, PersonDetail, PersonCreate

urlpatterns = [
	path('', PersonList.as_view(), name='personlist'),
	path('pd/pk=<int:pk>', PersonDetail.as_view(), name='persondetail'),
	path('person-create/', PersonCreate.as_view(), name='personcreate'),
]