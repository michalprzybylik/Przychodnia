from django.db import models

from common.models import User

from common.models import CommonProfileModel

# Create your models here.


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
        verbose_name_plural = "Kierownicy laboratorium"