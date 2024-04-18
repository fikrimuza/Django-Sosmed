from django import forms 

from .models import Picture, Comment

class PictureForm(forms.ModelForm):
	class Meta:
		model = Picture
		fields = [
			'user',
			'pictures',
			'caption',
			'category',
		]

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = [
			'user',
			'picture',
			'comment',
		]