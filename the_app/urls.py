from django.urls import path
from . import views
# from .views import PersonList

urlpatterns = [
	# path('', PersonList.as_view(), name='personlist'),
	path('', views.persons, name='persons')	
]