from django.contrib import admin
from apitest.models import Apis
# Register your models here.

from product.models import Product


class ApisAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'create_time', 'id',
                    'product']
    model = Apis
    extra = 1


# admin.site.register(Product,ProductAdmin)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('productname', 'productdesc', 'producter', 'create_time', 'id')
    inlines = [ApisAdmin]
