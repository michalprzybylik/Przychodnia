from django.contrib import admin

from przychodnia_pacjent import models


@admin.register(models.Pacjent)
class PacjentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Adres)
class AdresAdmin(admin.ModelAdmin):
    pass
