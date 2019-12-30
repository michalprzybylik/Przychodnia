from django.contrib import admin

from przychodnia_wizyta.models import Wizyta


@admin.register(Wizyta)
class WizytaAdmin(admin.ModelAdmin):
    list_filter = ["status"]
    ordering = ["dt_rej"]
    search_fields = ["pacjent", "rejestratorka", "lekarz"]
    list_display = [
        "dt_rej", "status", "dt_zak_anul", "rejestratorka", "lekarz", "pacjent"
    ]
