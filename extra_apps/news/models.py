# -*- coding:utf-8 -*-
from django.db import models

from DjangoUeditor.models import UEditorField
from datetime import datetime
# Create your models here.



class Category(models.Model):
    name = models.CharField(verbose_name=u"栏目名称",max_length=50,blank=False,null=False)
    en_name = models.CharField(verbose_name=u"栏目英文名称",max_length=50,blank=False,null=False)
    index = models.IntegerField(verbose_name=u"顺序",default=100)
    display = models.CharField(verbose_name=u"是否显示", max_length=1, default='1', choices=(('0', '隐藏'), ('1', '显示')))
    add_time = models.DateTimeField(verbose_name=u"新增时间",default=datetime.now)

    class Meta:
        verbose_name = u"新闻栏目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name




class News(models.Model):
    title = models.CharField(verbose_name=u"新闻标题",max_length=100,blank=False,null=False)
    en_title = models.CharField(verbose_name=u"英文新闻标题",max_length=100,blank=False,null=False)
    surface_plot = models.ImageField(verbose_name=u"封面图",max_length=100,upload_to="news/%Y/%m")
    category = models.ForeignKey(Category,verbose_name=u"栏目")
    author = models.CharField(verbose_name=u"作者",max_length=50)
    summary = models.TextField(verbose_name=u"新闻概要",default="")
    en_summary = models.TextField(verbose_name=u"英文新闻概要",default="")
    content = UEditorField(verbose_name=u"内容",width=900,height=500,filePath="content/ueditor/",imagePath="content/ueditor",default="",toolbars="full")
    en_content = UEditorField(verbose_name=u"英文内容",width=900,height=500,toolbars="full",default="",imagePath="content/ueditor/",filePath="content/ueditor/")
    display = models.CharField(verbose_name=u"是否显示", max_length=1, default='1', choices=(('0', '隐藏'), ('1', '显示')))
    add_time = models.DateTimeField(verbose_name=u"发布时间",default=datetime.now)

    class Meta:
        verbose_name = u"新闻"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title