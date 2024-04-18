from django.db import models

from django.urls import reverse
from user.models import User


# Create your models here.
class Picture(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	pictures = models.ImageField(upload_to='upload/')
	caption = models.CharField(max_length=200, blank=True)

	category_list = (
			('art', 'art'),
			('calligraphy', 'calligraphy'),
			('canva art', 'canva art'),
			('caricature', 'caricature'),
			('cartoon', 'cartoon'),
			('comic', 'comic'),
			('doodle', 'doodle'),
			('graffity', 'graffity'),
			('line art', 'line art'),
			('photography', 'photography'),
			('sketch', 'sketch'),
			('vector', 'vector'),
			('vinyet', 'vinyet'),
		)
	category = models.CharField(
			max_length=100,
			choices= category_list,
			default='art',
		)
	publish = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)
	comments = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='comments', blank=True, null=True)

	def  get_absolute_url(self):
		return reverse('art:list')

	def __str__(self):
		return (f'{self.caption}')


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	picture = models.ForeignKey('Picture', on_delete=models.CASCADE)
	comment = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return (f'{self.picture}. {self.comment}')
