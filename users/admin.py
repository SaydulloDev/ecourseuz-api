from django.contrib import admin

from .models import User, UserTypes


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']
    ordering = ['-date_joined']


admin.site.register(UserTypes)
