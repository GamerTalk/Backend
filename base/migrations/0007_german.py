# Generated by Django 4.2.1 on 2023-05-30 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_chinese'),
    ]

    operations = [
        migrations.CreateModel(
            name='german',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('user_uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.users')),
            ],
        ),
    ]
