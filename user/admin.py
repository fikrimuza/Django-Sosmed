from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.
from .models import User

class AppUserAdmin(UserAdmin):
	fieldsets = (
			(None, 
				{'fields': (
					'email', 
					'password', 
					'name',
					'user_picture',
					)
				}
			),

			('Permissions', 
				{'fields': (
					'is_active', 
					'is_staff', 
					'is_superuser', 
					'groups', 
					'user_permissions',
					)
				}
			),
		)

	add_fieldsets = (
			(None, 
				{
				'classes': ('wide',),
				'fields': ('email', 'password1', 'password2')
				}
			),
		)

	list_display = ('email', 'name', 'is_staff', 'last_login')
	list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ('groups', 'user_permissions')


admin.site.register(User, AppUserAdmin)