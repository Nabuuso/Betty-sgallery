# Generated by Django 3.2.9 on 2021-12-02 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lizgalleryapp', '0003_alter_image_image_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image_name'], 'verbose_name': 'My gallery', 'verbose_name_plural': 'galleries'},
        ),
    ]
