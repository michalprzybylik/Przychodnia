from django.contrib import admin
from laboratorium_app import models

@admin.register(models.Laborant)
class LaborantAdmin(admin.ModelAdmin):
    pass


@admin.register(models.KierownikLabarotorium)
class KierownikLabarotoriumAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BadanieLaboratoryjne)
class BadanieLaboratoryjneAdmin(admin.ModelAdmin):
    pass
