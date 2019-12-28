from django.db import models

from common.models import User

from common.models import CommonProfileModel, SlownikBadan


class Laborant(CommonProfileModel):
    # Połączenie z głównym modelem użytkownika
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    role = models.CharField(max_length=16, default="LABORANT", editable=False)

    class Meta:
        verbose_name_plural = "Laboranci"

class KierownikLabarotorium(CommonProfileModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    role = models.CharField(max_length=16, default="KIERLAB", editable=False)

    class Meta:
        verbose_name_plural = "Kierownicy Laboratorium"

class BadanieLaboratoryjne(models.Model):
    STATUS = (
        ("ZLE", "Zlecone"),
        ("WYK", "Wykonane"),
        ("ANUL_LAB", "Anulowane przez Laboranta"),
        ("ZATW", "Zatwierdzone"),
        ("ANUL_KLAB", "Anulowane przez Kier. Laboratorium"),
    )
    status = models.CharField(
        null=False, choices=STATUS, max_length=9, default="ZLE"
    )
    uwagi_lekarza = models.TextField(null=True, blank=True)
    dt_zlecenia = models.DateTimeField(auto_now_add=True)
    # TODO: Wynik w sensie pozytywny(true)/negatywny(false) BooleanField,
    #       czy jako TextField ?
    wynik = models.BooleanField(default=False)
    # Data wykonania/anulowania przez Laboranta
    dt_wyk_anul_lab = models.DateTimeField(null=True)
    # Data zatwierdzenia/anulowania przez Kier. Laboratorium
    dt_zatw_anul_klab = models.DateTimeField(null=True)
    uwagi_kierownika = models.TextField(null=True, blank=True)
    slownik = models.ForeignKey(SlownikBadan, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Badania Laboratoryjne"
