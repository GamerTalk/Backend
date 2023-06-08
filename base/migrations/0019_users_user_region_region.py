# Generated by Django 4.2.1 on 2023-06-08 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_users_user_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_region',
            field=models.TextField(default=str),
        ),
        migrations.CreateModel(
            name='region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.TextField()),
                ('user_uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.users', to_field='uid')),
            ],
        ),
    ]
