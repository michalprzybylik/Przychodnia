from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        ('REJ', 'REJESTRATORKA'),
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

    @property
    def name_with_role(self):
        return "%s %s [%s]" % (self.imie, self.nazwisko, self.role)

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

    class Meta:
        verbose_name_plural = "Słownik Badań"
