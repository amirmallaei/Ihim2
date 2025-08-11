from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    # Specify fields to show in admin list view
    list_display = ('email','phone_number', 'username', 'is_staff', 'is_active', 'date_joined')

    # Mark date_joined as readonly so it can be displayed but not edited
    readonly_fields = ('date_joined',)

    # Define the fields to include in the user edit form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'username')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, UserAdmin)