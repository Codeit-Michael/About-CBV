from django.urls import path
from .views import PersonList, PersonDetail, PersonCreate, PersonDelete, PersonUpdate, UserLogin, UserSignup
from django.contrib.auth.views import LogoutView

urlpatterns = [
	path('signup/', UserSignup.as_view(), name='signup'),
	path('signin/', UserLogin.as_view(), name='signin'),
	path('signout/', LogoutView.as_view(next_page='signin'), name='signout'),
	path('person-list', PersonList.as_view(), name='personlist'),
	path('person-delete/pk=<int:pk>', PersonDelete.as_view(), name='persondelete'),
	path('person-detail/pk=<int:pk>', PersonDetail.as_view(), name='persondetail'),
	path('person-create/', PersonCreate.as_view(), name='personcreate'),
	path('person-update/pk=<int:pk>', PersonUpdate.as_view(), name='personupdate'),
]