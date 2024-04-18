from django.urls import path 

from . import views

app_name = 'art'
urlpatterns = [
	path('delete/<pk>', views.PictureDeleteView.as_view(), name='delete'),
	path('update/<pk>', views.PictureUpdateView.as_view(), name='update'),
	path('create', views.PictureCreateView.as_view(), name='create'),
	path('category/<category>', views.PictureCategoryView.as_view(), name='category'),
	
	path('<page>', views.PictureListView.as_view(), name='list'),
	path('', views.PictureListView.as_view(), name='list'),
]