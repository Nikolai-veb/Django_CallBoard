# Generated by Django 3.0.5 on 2020-07-05 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200705_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='profile/', verbose_name='Аватар'),
        ),
    ]