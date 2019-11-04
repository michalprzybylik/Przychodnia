from django.contrib import admin

from przychodnia_app import models


@admin.register(models.Rejestratorka)
class RejestratorkaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Lekarz)
class LekarzAdmin(admin.ModelAdmin):
    pass
