from django.contrib import admin
from set.models import Set
# Register your models here.

class SetAdmin(admin.ModelAdmin):
    list_display = ['setname','setvalue','id']

admin.site.register(Set)