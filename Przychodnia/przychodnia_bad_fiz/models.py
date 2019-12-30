from django.db import models

from common.models import User, CommonProfileModel, SlownikBadan
from przychodnia_wizyta.models import Wizyta


class BadanieFizykalneQuerySet(models.QuerySet):
    def w_ramach_wizyty(self, wizyta):
        return self.filter(
            wizyta=wizyta.id
        )


class BadanieFizykalneManager(models.Manager):
    def get_queryset(self):
        return BadanieFizykalneQuerySet(self.model, using=self._db)

    def w_ramach_wizyty(self, wizyta):
        return self.get_queryset().w_ramach_wizyty(wizyta)


class BadanieFizykalne(models.Model):
    slownik = models.ForeignKey(SlownikBadan, on_delete=models.PROTECT)
    wizyta = models.ForeignKey(Wizyta, on_delete=models.PROTECT)
    # TODO: Wynik w sensie pozytywny(true)/negatywny(false) BooleanField,
    #       czy jako TextField ?
    # wynik = models.BooleanField(default=False)
    wynik = models.TextField()

    badania = BadanieFizykalneManager()

    class Meta:
        verbose_name_plural = "Badania Fizykalne"
