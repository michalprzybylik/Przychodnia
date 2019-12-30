from django.contrib import admin

from przychodnia_app import models


@admin.register(models.Rejestratorka)
class RejestratorkaAdmin(admin.ModelAdmin):
    search_fields = ["imie", "nazwisko"]
    list_display = ["__str__", "user"]


@admin.register(models.Lekarz)
class LekarzAdmin(admin.ModelAdmin):
    search_fields = ["imie", "nazwisko"]
    list_display = ["__str__", "user"]
