# Generated by Django 2.0.4 on 2018-04-16 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0002_auto_20180416_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followers', to='logic.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_kweets', to='logic.Kweet'),
        ),
    ]
