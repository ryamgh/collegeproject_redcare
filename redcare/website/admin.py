

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as baseUserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm

class CustomUserAdmin(baseUserAdmin):
   admin.site.register(CustomUser)

