from django.db import models
from mdeditor.fields import MDTextField
from django.utils.html import mark_safe
from markdown import markdown


class FlowPath(models.Model):
    """ 流程名称 """
    name = models.CharField(max_length=20, verbose_name='流程名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '流程名称'
        verbose_name_plural = verbose_name


class Step(models.Model):
    """ 步骤 """
    flow_path = models.ForeignKey("FlowPath", on_delete=models.CASCADE, verbose_name='流程名称')
    step_name = models.CharField(max_length=30, verbose_name='步骤名称')
    step_detail = MDTextField(verbose_name='步骤说明')

    def __str__(self):
        return self.step_name

    def step_detail_md(self):
        """ 转化为 markdown """
        return mark_safe(markdown(self.step_detail))

    class Meta:
        verbose_name = '步骤'
        verbose_name_plural = verbose_name
