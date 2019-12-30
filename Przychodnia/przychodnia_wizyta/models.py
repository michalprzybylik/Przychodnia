from datetime import timedelta

from django.db import models
from django.db.models import Q
from django.utils import timezone

from przychodnia_pacjent.models import Pacjent
from przychodnia_app.models import Lekarz, Rejestratorka


class WizytaQuerySet(models.QuerySet):
    def get_old(self):
        return self.filter(
            Q(status='REJ') & Q(dt_rej__lte=timezone.now() - timedelta(hours=12)))

    def get_new(self):
        return self.filter(
            Q(status='REJ') & Q(dt_rej__gte=timezone.now() - timedelta(hours=12)))

    def filter_by_lekarz(self, user, typ):
        return self.filter(
            Q(status=typ) & Q(lekarz=user))

    def inne_wizyty_pacjenta(self, wizyta):
        return self.filter(pacjent=wizyta.pacjent).exclude(id=wizyta.id)


class WizytaManager(models.Manager):
    def get_queryset(self):
        return WizytaQuerySet(self.model, using=self._db)

    def get_old(self):
        return self.get_queryset().get_old()

    def get_new(self):
        return self.get_queryset().get_new()

    def filter_by_lekarz(self, user, typ="REJ"):
        return self.get_queryset().filter_by_lekarz(user, typ)

    def inne_wizyty_pacjenta(self, wizyta):
        return self.get_queryset().inne_wizyty_pacjenta(wizyta)

class Wizyta(models.Model):
    STATUS = (
        ("REJ", "Zarejestrowana"),
        ("ZAK", "Zakończona"),
        ("ANUL", "Anulowana")
    )
    opis = models.TextField(null=True, blank=True)
    diagnoza = models.TextField(null=True, blank=True)
    status = models.CharField(null=False, choices=STATUS, max_length=4, default="REJ")
    dt_rej = models.DateTimeField(auto_now_add=True)
    dt_zak_anul = models.DateTimeField(null=True, blank=True)

    pacjent = models.ForeignKey(Pacjent, on_delete=models.PROTECT)
    rejestratorka = models.ForeignKey(Rejestratorka, on_delete=models.PROTECT)
    lekarz = models.ForeignKey(Lekarz, on_delete=models.PROTECT)

    wizyty = WizytaManager()

    @property
    def is_old(self): # czy wizyta jest 'stara'
        ret = self.status=='REJ'
        ret = ret and (self.dt_rej <= timezone.now() - timedelta(hours=12))
        return ret

    class Meta:
        ordering = ["dt_rej"]
        verbose_name_plural = "Wizyty"
