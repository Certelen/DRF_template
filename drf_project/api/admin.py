from django.contrib import admin

from api.models import Ad, Check


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
