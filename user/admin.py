from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserModelAdmin(UserAdmin):
    list_display = (
        'first_name',
        'last_name',
        'username',
        'email',
        'phone_number',
        'last_login',
    )
    readonly_fields = ('last_login',)
    fieldsets = ()


admin.site.register(User, UserModelAdmin)
