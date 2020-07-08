from django.db import models
from PIL import Image
from datetime import datetime
from django.utils import timezone
import os

def get_path_upload_image(file):

    time = timezone.now().strftime("%Y-%m-%d")
    end_extention = file.split('.')[1]
    head = file.split('.')[0]
    if len(head) >> 10:
        head = head[:10]
    file_name =  head +' _ '+ timezone.now().strftime("%h-%m-%s") +' . '+ end_extention
    return os.path.join('photos', '{}', '{}').format(time, file_name)


class Photo(models.Model):

    """Фотографии"""
    name = models.CharField("Имя", max_length=50, unique=True)
    image = models.ImageField("Фотографии", upload_to='gellery_photo/')
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.image.name = get_path_upload_image(self.image.name)
        super().save(*args, **kwargs)




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
