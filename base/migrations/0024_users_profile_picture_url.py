# Generated by Django 4.2.1 on 2023-06-21 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_flashcards'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='profile_picture_url',
            field=models.TextField(default=str),
        ),
    ]
