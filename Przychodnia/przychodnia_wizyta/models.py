from django.db import models

from przychodnia_pacjent.models import Pacjent
from przychodnia_app.models import Rejestratorka
from przychodnia_app.models import Lekarz

class Wizyta(models.Model):
    STATUS = (
        ("REJ", "Zarejestrowana"),
        ("ZAK", "Zakończona"),
        ("ANUL", "Anulowana")
    )
    opis = models.TextField()
    diagnoza = models.TextField()
    status = models.CharField(null=False, choices=STATUS, max_length=4, default="REJ")
    dt_rej = models.DateTimeField(auto_now_add=True)
    dt_zak_anul = models.DateTimeField(null=True)

    pacjent = models.ForeignKey(Pacjent, on_delete=models.PROTECT)
    rejestratorka = models.ForeignKey(Rejestratorka, on_delete=models.PROTECT)
    lekarz = models.ForeignKey(Lekarz, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Wizyty"
