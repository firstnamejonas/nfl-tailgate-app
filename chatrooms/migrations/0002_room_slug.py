# Generated by Django 4.2.10 on 2024-03-08 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatrooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
    ]