from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .manager import UserManager
from .generator import username_generator


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length=254, unique=True)
	name = models.CharField(max_length=255)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	last_login = models.DateTimeField(null=True, blank=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	user_picture = models.ImageField(upload_to='profile/', default='profile/user_picture.png')

	# setting Filed
	USERNAME_FIELD = 'email'
	EMAIL_FIELD = 'email'
	REQUIRED_FIELDS = []

	# User Manager
	objects = UserManager() 

	class Meta:
		abstract = False

	def save(self, *args, **kwargs):
		if self.name == '':
			self.name = username_generator(self.email)
			return super().save(*args, **kwargs)