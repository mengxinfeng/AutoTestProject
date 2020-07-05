from django.contrib import admin

# Register your models here.

from apitest.models import Apitest, Apistep, Apis


# TabularInline --横向的以表格的形式展示数据
class ApistepAdmin(admin.TabularInline):
    list_display = ['apistep', 'apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus',
                    'create_time', 'id']
    model = Apistep
    extra = 1


class ApitestAdmin(admin.ModelAdmin):
    list_display = ['apitestname', 'apitester', 'apitestresult', 'create_time', 'id']
    inlines = [ApistepAdmin]


class ApisAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'create_time', 'id',
                    'product']


admin.site.register(Apitest, ApitestAdmin)
admin.site.register(Apis)
