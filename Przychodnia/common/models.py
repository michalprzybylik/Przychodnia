from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        ('REJ', 'REJESTRATORKA'),
        ('ADM', 'ADMIN'),
        ('LEK', 'LEKARZ'),
        ('LAB', 'LABORANT'),
        ('KLAB', 'KIEROWNIK LABORATORIUM')
    )
    role = models.CharField(null=True, max_length=16, choices=ROLES)


class CommonProfileModel(models.Model):
    imie = models.CharField("Imię", max_length=32)
    nazwisko = models.CharField("Nazwisko", max_length=32)

    def __str__(self):
        return "%s %s" % (self.imie, self.nazwisko)

    class Meta:
        abstract = True


class SlownikBadan(models.Model):
    TYP_BAD = (
        ('L', 'Laboratoryjne'),
        ('F', 'Fizykalne'),
    )
    key = models.CharField(max_length=32, primary_key=True)
    typ = models.CharField(max_length=1, choices=TYP_BAD)
    nazwa = models.CharField(max_length=128)

    def __str__(self):
        return "{s.key} - {s.nazwa}".format(s=self)

    class Meta:
        verbose_name_plural = "Słownik Badań"
