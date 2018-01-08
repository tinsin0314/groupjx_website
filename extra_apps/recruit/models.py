# -*- coding:utf-8 -*-
from django.db import models

from DjangoUeditor.models import UEditorField
from datetime import datetime
# Create your models here.


class Recruit(models.Model):
    job_name = models.CharField(verbose_name=u"岗位名称",max_length=50,null=False,blank=False)
    en_job_name = models.CharField(verbose_name=u"英文岗位名称",max_length=50,null=False,blank=False)
    job_nums = models.IntegerField(verbose_name=u"招聘数量",default=1)
    job_desc = UEditorField(verbose_name=u"岗位职责",toolbars="full",default="",imagePath="recruit/ueditor/",filePath="recruit/ueditor/",width=900,height=500)
    en_job_desc = UEditorField(verbose_name=u"英文岗位职责",toolbars="full",default="",imagePath="recruit/ueditor/",filePath="recruit/ueditor/",width=900,height=500)
    requirements = UEditorField(verbose_name=u"任职要求",toolbars="full",default="",imagePath="recruit/ueditor/",filePath="recruit/ueditor/",width=900,height=500)
    en_requirements = UEditorField(verbose_name=u"英文任职要求",toolbars="full",default="",imagePath="recruit/ueditor/",filePath="recruit/ueditor/",width=900,height=500)
    index = models.IntegerField(verbose_name=u"顺序",default=100)
    display = models.CharField(verbose_name=u"是否显示", max_length=1, default='1', choices=(('0', '隐藏'), ('1', '显示')))
    add_time = models.DateTimeField(verbose_name=u"发布时间", default=datetime.now)

    class Meta:
        verbose_name = "招聘岗位"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.job_name

