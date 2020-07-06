from django.contrib import admin

from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "email_two", "avatar")
    prepopulated_fields = {"slug":("first_name",)}



