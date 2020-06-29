from django.db import models

# Create your models here.

class Product(models.Model):
    # 产品名称
    productname = models.CharField('产品名称',max_length=64)
    # 产品描述
    productdesc = models.CharField('产品描述',max_length=200)
    # 产品负责人
    producter = models.CharField('产品负责人',max_length=200)
    # 创建时间，自动获取当前时间
    create_time = models.DateTimeField('创建时间',auto_now=True)

    class Meta:
        verbose_name = '产品管理'
        verbose_name_plural = '产品管理'
    def __str__(self):
        return self.productname
