from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
	FormView,
	)
from .models import Picture, Comment
from .forms import PictureForm, CommentForm


# Create your views here.
# VIEW
class PictureListView(FormView, ListView):
	model = Picture
	form_class = CommentForm
	ordering = ['publish']
	paginate_by = 10
	context_object_name = 'picture_list'
	extra_context = {
		'page_title': 'YOUTH | Art'
	}
	success_url = reverse_lazy('art:list')

	def form_valid(self, form):
		# print(form.cleaned_data)
		form.save()
		return super().form_valid(form)

	def get_context_data(self, *args, **kwargs):
		category_list = self.model.objects.values_list('category', flat=True).distinct()
		self.kwargs.update({'category_list': category_list})
		kwargs = self.kwargs
		return super().get_context_data(*args, **kwargs)


# CATEGORY VIEW
class PictureCategoryView(ListView):
	model = Picture
	template_name = "art/picture_category.html"
	context_object_name = 'picture_category'
	paginate_by = 5
	extra_context = {
		'page_title': 'YOUTH | Category Art'
	}

	def get_queryset(self):
		self.queryset = self.model.objects.filter(category=self.kwargs['category'])
		return super().get_queryset()

	def get_context_data(self, *args, **kwargs):
		category_list = self.model.objects.values_list('category', flat=True).distinct().exclude(category=self.kwargs['category'])
		self.kwargs.update({'category_list': category_list})
		kwargs = self.kwargs
		return super().get_context_data(*args, **kwargs)


# CREATE VIEW
class PictureCreateView(CreateView):
	model = Picture
	template_name = "art/picture_create.html"
	fields = [
		'user',
		'pictures',
		'caption',
		'category',
	]

	extra_context = {
		'page_title': 'YOUTH | Create'
	}


#UPDATE VIEW
class PictureUpdateView(UpdateView):
	model = Picture
	form_class = PictureForm
	template_name = 'art/picture_update.html'
	extra_context = {
		'page_title': 'YOUTH | Update'
	}


# DELETE VIEW
class PictureDeleteView(DeleteView):
	model = Picture
	success_url = reverse_lazy('art:list')
	extra_context = {
		'page_title': 'YOUTH | Delete'
	}
