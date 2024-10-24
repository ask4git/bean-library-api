from django.contrib import admin

from beanlibapi.apps.core.models import Bean


@admin.register(Bean)
class BeanAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'region', 'variety', 'process',)
    search_fields = ['uid', 'name']
