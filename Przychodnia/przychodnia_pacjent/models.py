from django.db import models
from common.models import CommonProfileModel

class Adres(models.Model):
    miejscowosc = models.CharField("Miejscowość", max_length=32)
    ulica = models.CharField("Ulica", max_length=32)
    nr_domu = models.CharField("Numer domu", max_length=16)
    nr_lokalu = models.CharField("Numer Lokalu", max_length=16)

    def __str__(self):
        return "%s, %s %s/%s" % (self.miejscowosc, self.ulica, self.nr_domu, self.nr_lokalu)

    class Meta:
        verbose_name_plural = "Adresy Zamieszkania"


class Pacjent(CommonProfileModel):
    adres = models.ForeignKey(Adres, on_delete=models.PROTECT)
    pesel = models.CharField("PESEL", max_length=11, unique=True)

    def __str__(self):
        return "%s %s (%s)" % (self.imie, self.nazwisko, self.pesel)

    class Meta:
        verbose_name_plural = "Pacjenci"
