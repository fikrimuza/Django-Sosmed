from django.db import models

from django.utils.text import slugify
from django.urls import reverse
from user.models import User


# Create your models here.
class Article(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	penulis = models.CharField(max_length=255)
	judul = models.CharField(max_length=255, unique=True)
	isi = models.TextField()

	category_list = (
			('article', 'article'),
			('drama', 'drama'),
			('fairytale', 'fairytale'),
			('novel', 'novel'),
			('poetry', 'poetry'),
			('romance', 'romance'),
			('sort story', 'sort story'),
		)

	kategori = models.CharField(
			max_length=100,
			choices=category_list,
			default='Article',
		)
	publish = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)
	slug = models.SlugField(blank=True, editable=False)

	def save(self):
		self.slug = slugify(self.judul)
		super().save()

	def get_absolute_url(self):
		url_slug = {
			'slug':self.slug,
		}
		return reverse('blog:detail', kwargs=url_slug)

	def __str__(self):
		return (f'{self.id}. {self.judul}')
