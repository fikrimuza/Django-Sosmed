from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount
from django.db.models.signal import pre_save


@receiver(pre_save, sender=SocialAccount)
def add_username(sender, instance, *args, **kwargs):
	user = instance.user 
	if user.name == '':
		extra_data = instance.extra_data
		name = extra_data['name']
		user.name = name 
		user.save()

