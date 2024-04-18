from django.contrib import admin

from . import models


# Register your models here.
class PictureAdmin(admin.ModelAdmin):
	readonly_fields = [
		'publish',
		'update',
	]

class CommentAdmin(admin.ModelAdmin):
	pass

admin.site.register(models.Picture, PictureAdmin)
admin.site.register(models.Comment, CommentAdmin)

