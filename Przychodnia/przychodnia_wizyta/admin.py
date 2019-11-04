from django.contrib import admin

from przychodnia_wizyta.models import Wizyta


@admin.register(Wizyta)
class WizytaAdmin(admin.ModelAdmin):
    pass
