# Generated by Django 2.0.4 on 2018-04-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(related_name='followers', to='logic.Profile'),
        ),
    ]
