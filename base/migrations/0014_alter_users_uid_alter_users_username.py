# Generated by Django 4.2.1 on 2023-05-31 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_users_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='uid',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]