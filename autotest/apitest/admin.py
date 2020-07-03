from django.contrib import admin

# Register your models here.

from apitest.models import Apitest, Apistep


# TabularInline --横向的以表格的形式展示数据
class ApistepAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'create_time', 'id',
                    'apitest']
    model = Apistep
    extra = 1


@admin.register(Apitest)
class ApitestAdmin(admin.ModelAdmin):
    list_display = ['apitestname', 'apitester', 'apitestresult', 'create_time', 'id']
    inlines = [ApistepAdmin]
