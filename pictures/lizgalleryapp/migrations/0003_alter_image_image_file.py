# Generated by Django 3.2.9 on 2021-12-02 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lizgalleryapp', '0002_auto_20211201_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(null=True, upload_to='Images/'),
        ),
    ]
