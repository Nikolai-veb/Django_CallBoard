from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, FilterAdvert, DateAdvert, Advert

@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    """Категории"""
    list_display = ("name", "id", "parent")
    mptt_level_indent = 20
    prepopulated_fields = {"slug":("name",)}
    search_fields = ("name", "parent")

@admin.register(FilterAdvert)
class FilterAdvertAdmin(admin.ModelAdmin):
    """Предстовление фильтра обновленияи"""
    list_display = ("id", "name")
    list_display_links = ("name",)
    prepopulated_fields = {"slug":("name",)}
    search_fields = ("name", )

@admin.register(DateAdvert)
class DateAdvertAdmin(admin.ModelAdmin):
    """Фильтр обновлений"""
    list_display = ("id", "name")
    list_display_links = ("name",)
    prepopulated_fields = {"slug":("name",)}
    search_fields = ("name", )


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    """Объявления"""
    list_display = (
            "id",
            "images",
            "subject",
            "user",
            "category",
            "filtres",
            "date",
            "description",
            "price",
            "moderation",
            "files",
            "created",
            )
    list_display_links = ("subject",)
    list_filter = ("category", "filtres", "date", "price")
    prepopulated_fields = {"slug":("subject",)}
    search_fields = ("category", "subject")
