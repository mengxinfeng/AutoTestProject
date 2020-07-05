from django.contrib import admin

# Register your models here.

from bug.models import Bug

class BugAdmin(admin.ModelAdmin):
    list_display = ['bugname', 'bugdetail', 'bugstatus', 'buglevel', 'bugcreater', 'bugassign', 'create_time','id']

admin.site.register(Bug)