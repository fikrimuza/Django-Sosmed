from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
	def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
		if not email:
			raise ValueError('User Mush Have Email')
		now = timezone.now()
		email = self.normalize_email(email)
		user = self.model(
				email=email,
				is_staff=is_staff,
				is_superuser=is_superuser,
				is_active=True,
				last_login=now,
				date_joined=now,
				**extra_fields
			)

		# set password
		user.set_password(password)
		user.save(using=self._db)
		return user 

	# create now user
	def create_user(self, email, password, **extra_fields):
		return self._create_user(email, password, False, False, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		user = self._create_user(email, password, True, True, **extra_fields)
		user.save(using=self._db)
		return user