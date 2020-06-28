from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User

class Category(MPTTModel):
    """Категории объявлений"""
    name = models.CharField("Имя", max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField('url', max_length=50)

    def __str__(self):
        return self.name


    class MPTTMeta:
        order_insertion_by=['name']


class FilterAdvert(models.Model):
    """Фильтр объявлений"""
    name = models.CharField("Имя", max_length=50, unique=True)
    slug = models.SlugField('url', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтры'


class DateAdvert(models.Model):
    """Фильтр объявлений"""
    name = models.CharField("Имя", max_length=50, unique=True)
    slug = models.SlugField('url', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Срок'
        verbose_name_plural = 'Сроки'
        ordering = ["-id"]


class Advert(models.Model):
    """Объявления"""
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    filtres = models.ForeignKey(FilterAdvert, verbose_name="Фильтры", on_delete=models.CASCADE)
    date = models.ForeignKey(DateAdvert, verbose_name="Сроки", on_delete=models.CASCADE)
    subject = models.CharField("Тема", max_length=200)
    discription = models.TextField("Объявление")
    images = models.ForeignKey(
            'gellery.Gellery',
            verbose_name="Фотографии",
            on_delete=models.SET_NULL,
            blank=True,
            null=True
            )
    files = models.FileField("Фаил", upload_to='callboard_file/', blank=True, null=True)
    prise = models.DecimalField("Цена", max_digits=8, decimal_places=2)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    moderation = models.BooleanField("Модерацыя", default=False)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
