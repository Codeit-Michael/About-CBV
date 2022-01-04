from django.urls import path
from . import views
from .views import PersonList, PersonDetail, PersonCreate, PersonDelete, PersonUpdate

urlpatterns = [
	path('person-list', PersonList.as_view(), name='personlist'),
	path('person-delete/pk=<int:pk>', PersonDelete.as_view(), name='persondelete'),
	path('person-detail/pk=<int:pk>', PersonDetail.as_view(), name='persondetail'),
	path('person-create/', PersonCreate.as_view(), name='personcreate'),
	path('person-update/pk=<int:pk>', PersonUpdate.as_view(), name='personupdate'),
	path('signup/', views.signup, name='signup'),
	path('signin/', views.signin, name='signin'),
	path('signout/', views.signout, name='signout'),
]