from django.urls import path
from . import views
from .views import PersonList, PersonDetail

urlpatterns = [
	path('', PersonList.as_view(), name='personlist'),
	path('pd/<int:pk>', PersonDetail.as_view(), name='persondetail'),
]