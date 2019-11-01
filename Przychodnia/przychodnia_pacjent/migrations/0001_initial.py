# Generated by Django 2.2.6 on 2019-11-01 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miejscowosc', models.CharField(max_length=32, verbose_name='Miejscowość')),
                ('ulica', models.CharField(max_length=32, verbose_name='Ulica')),
                ('nr_domu', models.CharField(max_length=16, verbose_name='Numer domu')),
                ('nr_lokalu', models.CharField(max_length=16, verbose_name='Numer Lokalu')),
            ],
        ),
        migrations.CreateModel(
            name='Pacjent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=32, verbose_name='Imie')),
                ('nazwisko', models.CharField(max_length=32, verbose_name='Nazwisko')),
                ('pesel', models.CharField(max_length=11, unique=True, verbose_name='PESEL')),
                ('adres', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='przychodnia_pacjent.Adres')),
            ],
        ),
    ]