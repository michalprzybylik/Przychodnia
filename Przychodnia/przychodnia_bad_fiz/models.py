from django.db import models

from common.models import User, CommonProfileModel, SlownikBadan
from przychodnia_wizyta.models import Wizyta

class BadanieFizykalne(models.Model):
    slownik = models.ForeignKey(SlownikBadan, on_delete=models.PROTECT)
    wizyta = models.ForeignKey(Wizyta, on_delete=models.PROTECT)
    # TODO: Wynik w sensie pozytywny(true)/negatywny(false) BooleanField,
    #       czy jako TextField ?
    wynik = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Badania Fizykalne"
