from django.db import models

class Photo(models.Model):
    """Фотографии"""
    name = models.CharField("Имя", max_length=50, unique=True)
    image = models.ImageField("Фотографии", upload_to='gellery_photo/')
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'

class Gellery(models.Model):
    """Галерея"""
    name = models.CharField("Имя", max_length=50, unique=True)
    photos =models.ManyToManyField(Photo, verbose_name="Фотографии")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'
