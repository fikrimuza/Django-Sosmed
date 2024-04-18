from django.shortcuts import render

from django.views.generic import ListView, DetailView
from art.models import Picture
from blog.models import Article
from .models import User


# Create your views here.
# MY PROFILE
def user_profile(request, pk):
	user = User.objects.get(id=pk)
	context = {
		'page_title': 'YOUTH | Profile',
	}
	return render(request, 'user/profile.html', context)

class ProfileListArt(ListView):
	model = Picture
	ordering = ['publish']
	template_name = 'user/profile_art.html'
	context_object_name = 'profile_art'
	extra_context = {
		'page_title': 'YOUTH | My Art'
	}

	def get_queryset(self):
		self.queryset = self.model.objects.filter(user = self.kwargs['pk'])
		return super().get_queryset()
	


class ProfileListBlog(ListView):
	model = Article
	ordering = ['publish']
	template_name = 'user/profile_blog.html'
	context_object_name = 'profile_blog'
	extra_context = {
		'page_title': 'YOUTH | My Wrote'
	}

	def get_queryset(self):
		self.queryset = self.model.objects.filter(user = self.kwargs['pk'])
		return super().get_queryset()

# GUEST
def user_guest(request, pk):
	user = User.objects.get(id=pk)
	context = {
		'user':user,
	}
	return render(request, 'user/guest.html', context)