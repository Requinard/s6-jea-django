# Generated by Django 2.0.4 on 2018-04-16 15:43
from datetime import datetime

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logic', '0005_auto_20180416_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_edited',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kweet',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='kweet',
            name='last_edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
