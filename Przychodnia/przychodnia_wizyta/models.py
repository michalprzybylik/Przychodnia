from datetime import timedelta

from django.db import models
from django.db.models import Q
from django.utils import timezone

from przychodnia_pacjent.models import Pacjent
from przychodnia_app.models import Rejestratorka
from przychodnia_app.models import Lekarz


class WizytaQuerySet(models.QuerySet):
    def get_old(self):
        return self.filter(
            Q(status='REJ') & Q(dt_rej__lte=timezone.now() - timedelta(hours=12)))

    def get_new(self):
        return self.filter(
            Q(status='REJ') & Q(dt_rej__gte=timezone.now() - timedelta(hours=12)))

class WizytaManager(models.Manager):
    def get_queryset(self):
        return WizytaQuerySet(self.model, using=self._db)

    def get_old(self):
        return self.get_queryset().get_old()

    def get_new(self):
        return self.get_queryset().get_new()

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

    wizyty = WizytaManager()

    class Meta:
        ordering = ["-dt_rej"]
        verbose_name_plural = "Wizyty"
