from django.db import models

# from django.contrib.auth.models import User
from common.models import User

from common.models import CommonProfileModel, SlownikBadan


class Rejestratorka(CommonProfileModel):
    # Połączenie z głównym modelem użytkownika
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    role = models.CharField(max_length=16, default="REJESTRATORKA", editable=False)

    class Meta:
        verbose_name_plural = "Rejestratorki"

class Lekarz(CommonProfileModel):
    # Połączenie z głównym modelem użytkownika
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    role = models.CharField(max_length=16, default="LEKARZ", editable=False)
    npwz = models.CharField("NPWZ", max_length=7, unique=True)

    class Meta:
        verbose_name_plural = "Lekarze"

class BadanieFizykalne(models.Model):
    slownik = models.ForeignKey(SlownikBadan, on_delete=models.PROTECT)
    # TODO: Wynik w sensie pozytywny(true)/negatywny(false) BooleanField,
    #       czy jako TextField ?
    wynik = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Badania Fizykalne"
