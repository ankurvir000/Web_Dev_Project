from django.contrib import admin
from .models import Profile

admin.site.register(Profile)

class adminProfile(admin.ModelAdmin):
    pass
