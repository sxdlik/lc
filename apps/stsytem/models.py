from django.db import models
from django.contrib.auth.models import AbstractUser


class Menu(models.Model):
    """ 菜单 """
    name = models.CharField(max_length=30, unique=True, verbose_name='菜单名')
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name='上级菜单')
    code = models.CharField(max_length=50, null=True, blank=True, verbose_name='编码')
    url = models.CharField(max_length=128, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = verbose_name


class Department(models.Model):
    """ 部门表 """
    department = models.CharField(max_length=16, unique=True, verbose_name='部门名称')
    type = models.CharField(max_length=4, choices=(('中心', '中心'), ('部门', '部门')), verbose_name='部门类型')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='上级部门')
    remarks = models.CharField(max_length=256, verbose_name='备注')

    def __str__(self):
        return self.department

    class Meta:
        ordering = ['department']
        verbose_name = '部门表'
        verbose_name_plural = verbose_name


