from django.views.generic import TemplateView
from user.models import User


class Homepage(TemplateView):
	model = User
	template_name = 'homepage.html'
	extra_context = {
		'page_title': 'YOUTH | Homepage'
	}

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user'] = User.objects.all()
		return super().get_context_data(**kwargs)


class Portfolio(TemplateView):
	template_name = 'Portfolio.html'
	extra_context = {
		'page_title': 'MUZA'
	}