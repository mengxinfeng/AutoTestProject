from django.db import models

# Create your models here.

from product.models import Product


# 业务场景接口表
class Apitest(models.Model):
    # 关联产品ID，其中product是应用名，Product是表名
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    # 流程接口名称
    apitestname = models.CharField('流程接口名称', max_length=64)
    # 流程接口描述
    apitestdesc = models.CharField('描述', max_length=64, null=True)
    # 测试负责人
    apitester = models.CharField('测试负责人',max_length=16)
    # 流程接口结果
    apitestresult = models.BooleanField('测试结果')
    # 创建时间,默认获取当前时间
    create_time = models.DateTimeField('创建时间', auto_now=True)

    # 数据库表名
    class Meta:
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程场景接口'

    def __str__(self):
        return self.apitestname


# 业务场景步骤接口用例表
class Apistep(models.Model):
    # 关联接口用例ID
    Apitest = models.ForeignKey(Apitest,on_delete=models.CASCADE)
    # 测试步骤
    apistep = models.CharField('测试步骤',max_length=100,null=True)
    # 接口标题
    apiname = models.CharField('接口名称',max_length=100)
    # 接口地址
    apiurl = models.CharField('url地址',max_length=200)
    # 请求参数和值
    apiparamvalue = models.CharField('请求参数和值',max_length=800)
    # 请求方法
    REQUEST_METHOD = (('get','get'),('post','post'),('delete','delete'),('patch','patch'))
    apimethod = models.CharField(verbose_name='请求方法',choices=REQUEST_METHOD,default='get',max_length=200,null=True)
    # 预期结果
    apiresult = models.CharField('预期结果',max_length=200)
    # 测试结果
    apistatus = models.BooleanField('是否通过')
    # 创建时间
    create_time = models.DateTimeField('创建时间',auto_now=True)

    def __str__(self):
        return self.apistep


# 单一接口表
class Apis(models.Model):
    # 关联产品ID，其中product是应用名，Product是表名
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    # 接口名称
    apiname = models.CharField('流程接口名称', max_length=100)
    # 接口描述
    apiurl = models.CharField('URL地址', max_length=200)
    # 请求参数和值
    apiparamvalue = models.CharField('请求参数和值', max_length=800)
    # 请求方法
    REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('delete', 'delete'), ('patch', 'patch'))
    apimethod = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD, default='get', max_length=200, null=True)
    # 预期结果
    apiresult = models.CharField('预期结果', max_length=200)
    # 流程接口结果
    apistatus = models.BooleanField('测试结果')
    # 创建时间,默认获取当前时间
    create_time = models.DateTimeField('创建时间', auto_now=True)

    # 数据库表名
    class Meta:
        verbose_name = '单一场景接口'
        verbose_name_plural = '单一场景接口'

    def __str__(self):
        return self.apiname




