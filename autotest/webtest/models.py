from django.db import models
from product.models import Product


# Create your models here.

# web用例表
class Webcase(models.Model):
    # 关联产品ID
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    # 测试用例名称
    webcasename = models.CharField('测试名称', max_length=64)
    # 测试结果
    webtestresult = models.BooleanField('测试结果')
    # 测试负责人
    webtester = models.CharField('测试负责人', max_length=16)
    # 创建时间
    create_time = models.DateTimeField('创建时间', auto_now=True)

    class Meta:
        verbose_name = 'web测试用例'
        verbose_name_plural = 'web测试用例'

    def __str__(self):
        return self.webcasename


# web用例步骤表
class Webcasestep(models.Model):
    # 关联接口ID
    Webcase = models.ForeignKey(Webcase,on_delete=models.CASCADE)
    # 测试用例标题
    webcasename = models.CharField('测试用例标题',max_length=200)
    # 测试步骤
    webteststep = models.CharField('测试步骤',max_length=200)
    # 测试对象名称
    webtestobjname = models.CharField('测试对象名称',max_length=200)
    # 定位方式
    webfindmethod = models.CharField('定位方式',max_length=200)
    # 控件元素
    webevelement = models.CharField('控件方式',max_length=800)
    # 操作方法
    webopmethod = models.CharField('操作方法',max_length=200)
    # 测试数据
    webtestdata = models.CharField('测试数据',max_length=200,null=True)
    # 验证数据
    webassertdata = models.CharField('验证数据',max_length=200)
    # 测试结果
    webtestresult = models.BooleanField('测试结果')
    # 创建时间
    create_time = models.DateTimeField('创建时间',auto_now=True)

    def __str__(self):
        return self.webcasename
