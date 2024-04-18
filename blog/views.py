from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import (
		ListView, 
		DetailView, 
		FormView,
		CreateView,
		UpdateView,
		DeleteView,
	)
from .models import Article
from .forms import ArticleForm


# Create your views here.
# LIST VIEW
class ArticleListView(ListView):
	model = Article
	ordering = ['publish']
	paginate_by = 20
	context_object_name = 'article_list' # Default: object_list
	extra_context = {
		'page_title': ' YOUTH | Wrote List',
	}

	def get_context_data(self, *args, **kwargs):
		kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
		self.kwargs.update({'kategori_list': kategori_list})
		kwargs = self.kwargs
		return super().get_context_data(*args, **kwargs)


# CATEGORY LIST
class ArticleCategoryView(ListView):
	model = Article
	template_name = "blog/article_category.html"
	context_object_name = 'article_category'
	paginate_by=10
	ordering = ['-publish']
	extra_context = {
		'page_title': 'YOUTH | Category',
	}

	def get_queryset(self):
		self.queryset = self.model.objects.filter(kategori=self.kwargs['kategori'])
		return super().get_queryset()

	def get_context_data(self, *args, **kwargs):
		kategori_list = self.model.objects.values_list('kategori', flat=True).distinct().exclude(kategori=self.kwargs['kategori'])
		self.kwargs.update({'kategori_list': kategori_list})
		kwargs = self.kwargs
		return super().get_context_data(*args, **kwargs)


# DETAIL VIEW
class ArticleDetailView(DetailView):
	model = Article
	context_object_name = 'article_detail' # Default: object
	extra_context = {
		'page_title': 'YOUTH | Detail Wrote',
	}

	def get_context_data(self, *args, **kwargs):
		kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
		self.kwargs.update({'kategori_list': kategori_list})

		else_article = self.model.objects.filter(kategori=self.object.kategori).exclude(id=self.object.id)
		self.kwargs.update({'else_article':else_article})

		kwargs = self.kwargs

		return super().get_context_data(**kwargs)


# CREATE VIEW
class ArticleCreateView(CreateView):
	model = Article
	fields = [
		'user',
		'judul',
		'isi',
		'penulis',
		'kategori',
	]
	template_name = 'blog/article_create.html'

	extra_context = {
		'page_title': 'YOUTH | Create Article',
	}

	# form_class = ArticleForm
	# template_name = 'blog/article_create.html'
	# success_url = reverse_lazy('blog:blog')
	# extra_context = {
	# 	'page_title': 'Create Article',
	# }


	# def get_context_data(self, *args, **kwargs):
	# 	kwargs.update(self.extra_context)
	# 	return super().get_context_data(*args, **kwargs)

	# def form_valid(self, form):
	# 	form.save()
	# 	return super().form_valid(form)


# UPDATE VIEW
class ArticleUpdateView(UpdateView):
	model = Article
	form_class = ArticleForm
	extra_context = {
		'page_title': 'YOUTH | Update',
	}


# DELETE VIEW
class ArticleDeleteView(DeleteView):
	model = Article
	extra_context = {
		'page_title': 'YOUTH | Delete'
	}
	success_url = reverse_lazy('blog:blog')
	

# def index(request):
# 	context = {
# 		'page_title' : 'Blog'
# 	}

# 	return render(request, 'blog/blog.html', context)