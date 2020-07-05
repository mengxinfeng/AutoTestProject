from django.db import models

# Create your models here.

class Set(models.Model):
    # 设置名称
    setname = models.CharField('系统名称',max_length=64)
    # 设置值
    setvalue = models.CharField('系统设置',max_length=200)
    class Meta:
        verbose_name = '系统设置'
        verbose_name_plural = '系统设置'
    def __str__(self):
        return self.setname
