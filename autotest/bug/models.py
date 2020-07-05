from django.db import models
from product.models import Product


# 业务场景接口表
class Bug(models.Model):
    # 关联产品ID，其中product是应用名，Product是表名
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    # Bug名称
    bugname = models.CharField('bug名称', max_length=64)
    # 详情
    bugdetail = models.CharField('详情', max_length=200)
    # 解决状态
    BUG_STATUS = (('激活', '激活'), ('已解决', '已解决'), ('已关闭', '已关闭'))
    bug_status = models.CharField(verbose_name='解决状态', choices=BUG_STATUS, default='激活', max_length=200, null=True)
    # 严重程度
    BUG_LEVEL = (('1', '1'), ('2', '2'), ('3', '3'))
    bug_level = models.CharField(verbose_name='严重程度', choices=BUG_LEVEL, default='3', max_length=200, null=True)
    # 创始人
    bug_creater = models.CharField('创建人',max_length=200)
    # 分配给谁
    bugassign = models.CharField('分配给',max_length=200)
    # 更新时间值
    create_time = models.DateTimeField('更新时间', auto_now=True)
    # 数据库表名
    class Meta:
        verbose_name = 'bug管理'
        verbose_name_plural = 'bug管理'

    def __str__(self):
        return self.bugname