from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
	path('category/<kategori>/<page>', views.ArticleCategoryView.as_view(), name='category'),
	path('category/<kategori>/', views.ArticleCategoryView.as_view(), name='category'),
	path('delete/<pk>', views.ArticleDeleteView.as_view(), name='delete'),
	path('update/<pk>', views.ArticleUpdateView.as_view(), name='update'),
	path('create/', views.ArticleCreateView.as_view(), name='create'),
	path('detail/<slug>', views.ArticleDetailView.as_view(),name='detail'),
	# path('', views.index, name='blog'),
	path('<page>', views.ArticleListView.as_view(), name='blog'),
	path('', views.ArticleListView.as_view(), name='blog'),
]