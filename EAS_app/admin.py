from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AllUser

class UserModel(UserAdmin):
    ordering = ('email',)


admin.site.register(AllUser, UserModel)