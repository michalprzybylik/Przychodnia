# Generated by Django 2.2.6 on 2019-11-01 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('przychodnia_pacjent', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adres',
            options={'verbose_name_plural': 'Adresy Zamieszkania'},
        ),
        migrations.AlterModelOptions(
            name='pacjent',
            options={'verbose_name_plural': 'Pacjenci'},
        ),
    ]
