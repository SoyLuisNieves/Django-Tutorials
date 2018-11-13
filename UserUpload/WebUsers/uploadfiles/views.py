from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.views.generic import CreateView

from uploadfiles.models import User

class HomeView(generic.ListView):
	context_object_name = 'user_list'
	template_name = 'home_page.html'

	def get_queryset(self):
		return User.objects.all()


class UserEntry(CreateView):
	model = User
	fields = ['username', 'user_avatar']