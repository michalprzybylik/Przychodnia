# Generated by Django 2.2.6 on 2020-01-18 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorium_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badanielaboratoryjne',
            name='wynik',
            field=models.TextField(blank=True),
        ),
    ]
