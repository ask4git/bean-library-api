from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from beanlibapi.core.models import User
from beanlibapi.core.models import Bean

admin.site.register(User, UserAdmin)


@admin.register(Bean)
class BeanAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'region', 'variety', 'process',)
    search_fields = ['uid', 'name']
