# Generated by Django 3.1.1 on 2020-09-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('House', '0004_remove_house_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='image',
            field=models.ImageField(blank=True, default='images/thh.jpg', null=True, upload_to='images/Houes'),
        ),
    ]