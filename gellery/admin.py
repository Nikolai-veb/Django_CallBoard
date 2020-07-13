from django.contrib import admin

from .models import Gellery, Photo

@admin.register(Gellery)
class Gellery(admin.ModelAdmin):
    """Галлерея"""
    list_display = ("id", "name", "created")
    list_display_links = ("name",)
    prepopulated_fields = {"slug":("name",)}
    search_fields = ("name", )


@admin.register(Photo)
class Photo(admin.ModelAdmin):
    """Изображение"""
    list_display = ("id", "name", "created")
    list_display_links = ("name",)
    prepopulated_fields = {"slug":("name",)}
    search_fields = ("name", )
