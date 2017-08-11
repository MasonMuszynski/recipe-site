from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import userprofile


class userprofileInline(admin.StackedInline):
    model = userprofile
    can_delete = False
    verbose_name_plural = 'userprofile'


class UserAdmin(BaseUserAdmin):
    inlines = (userprofileInline,)


# Re-registering UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)