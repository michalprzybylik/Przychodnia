from django.contrib import admin

from przychodnia_pacjent import models


@admin.register(models.Pacjent)
class PacjentAdmin(admin.ModelAdmin):
    # list_filter = []
    # ordering = []
    search_fields = ["imie", "nazwisko", "pesel", "adres"]
    list_display = ["pesel", "imie", "nazwisko", "adres"]


@admin.register(models.Adres)
class AdresAdmin(admin.ModelAdmin):
    search_fields = ["miejscowosc", "ulica", "nr_domu", "nr_lokalu"]
    list_display = ["__str__", "miejscowosc", "ulica", "nr_domu", "nr_lokalu"]
