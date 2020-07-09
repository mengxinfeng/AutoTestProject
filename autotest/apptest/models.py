from django.db import models


# Create your models here.
# 用例管理表
class Appcase(models.Model):
    # 关联产品ID
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    # 测试用例名称
    appcasename = models.CharField('用例名称', max_length=200)
    # 测试结果
    apptestresult = models.BooleanField('测试结果')
    # 执行人
    apptester = models.CharField('测试负责人', max_length=16)
    # 创建时间
    create_time = models.DateTimeField('创建时间', auto_now=True)

    class Meta:
        verbose_name = 'app测试用例'
        verbose_name_plural = 'app测试用例'

    def __str__(self):
        return self.appcasename
# 用例步骤表
class Appcasestep(models.Model):
    # 关联接口ID
    Appcase = models.ForeignKey(Appcase,on_delete=models.CASCADE)
    # 测试步骤
    appteststep = models.CharField('测试步骤',max_length=200)
    # 测试对象名称描述
    apptestobjname = models.CharField('测试对象名称描述',max_length=200)
    # 定位方式
    appfindmethod = models.CharField('定位方式',max_length=200)
    # 控件元素
    appevelement = models.CharField('控件元素',max_length=800)
    # 测试数据
    apptestdata = models.CharField('操作方法',max_length=200)
    # 验证数据
    appassertdata = models.CharField('验证数据',max_length=200)
    # 测试结果
    apptestresult = models.BooleanField('测试结果')
    # 创建时间
    create_time = models.DateTimeField('创建时间',auto_now=True)
    def __str__(self):
        return self.appteststep
