from django.contrib import admin
from laboratorium_app import models

@admin.register(models.Laborant)
class LaborantAdmin(admin.ModelAdmin):
    # list_filter = []
    # ordering = []
    search_fields = ["imie", "nazwisko"]
    list_display = ["__str__", "user"]


@admin.register(models.KierownikLabarotorium)
class KierownikLabarotoriumAdmin(admin.ModelAdmin):
    # list_filter = []
    # ordering = []
    search_fields = ["imie", "nazwisko"]
    list_display = ["__str__", "user"]


@admin.register(models.BadanieLaboratoryjne)
class BadanieLaboratoryjneAdmin(admin.ModelAdmin):
    list_filter = ["status"]
    ordering = ["dt_zlecenia"]
    search_fields = ["laborant", "kier_lab"]
    list_display = ["dt_zlecenia", "status", "laborant", "kier_lab", "slownik"]
