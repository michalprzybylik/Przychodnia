from django.contrib import admin

from przychodnia_bad_fiz import models


@admin.register(models.BadanieFizykalne)
class BadanieFizykalneAdmin(admin.ModelAdmin):
    pass
