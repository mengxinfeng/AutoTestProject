from django.contrib import admin

# Register your models here.

from product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('productname','productdesc','producter','create_time','id')

# admin.site.register(Product,ProductAdmin)