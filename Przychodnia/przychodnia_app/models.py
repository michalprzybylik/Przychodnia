from django.db import models

# from django.contrib.auth.models import User
from common.models import User


class Rejestratorka(models.Model):
    # Połączenie z głównym modelem użytkownika
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    role = models.CharField(max_length=16, default="REJESTRATORKA", editable=False)

    imie = models.CharField("Imie", max_length=32)
    nazwisko = models.CharField("Nazwisko", max_length=32)

    def __str__(self):
        return "%s %s" % (self.imie, self.nazwisko)

    @property
    def name_with_role(self):
        return "%s %s [%s]" % (self.imie, self.nazwisko, self.role)

    class Meta:
        verbose_name_plural = "Rejestratorki"

class Lekarz(models.Model):
    # Połączenie z głównym modelem użytkownika
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    role = models.CharField(max_length=16, default="LEKARZ", editable=False)

    imie = models.CharField("Imie", max_length=32)
    nazwisko = models.CharField("Nazwisko", max_length=32)

    npwz = models.CharField("NPWZ", max_length=7, unique=True)

    class Meta:
        verbose_name_plural = "Lekarze"

    def __str__(self):
        return "%s %s" % (self.imie, self.nazwisko)
