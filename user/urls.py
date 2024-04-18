from django.urls import path 

from . import views

app_name = 'user'
urlpatterns = [
	path('wrote/<int:pk>', views.ProfileListBlog.as_view(), name='blog'),
	path('art/<int:pk>', views.ProfileListArt.as_view(), name='art'),
	path('profile/<int:pk>/', views.user_profile, name='profile'),
	path('profile/', views.user_profile, name='profile'),
]