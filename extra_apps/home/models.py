# -*- coding:utf-8 -*-
from django.db import models

from datetime import  datetime
# Create your models here.


class Banner(models.Model):
    title = models.CharField(verbose_name=u"标题",max_length=50,null=False,blank=False)
    image = models.ImageField(verbose_name=u"图片",upload_to="banners/%Y/%m",max_length=100,null=False,blank=False)
    url = models.CharField(verbose_name=u"URL链接",max_length=200,blank=True)
    index = models.IntegerField(verbose_name=u"顺序",default=100,blank=True)
    display = models.CharField(verbose_name=u"是否显示",max_length=1,default='1',choices=(('0','隐藏'),('1','显示')))
    add_time = models.DateTimeField(verbose_name=u"上传时间",default=datetime.now)

    class Meta:
        verbose_name = u"轮播"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title



class LearnMoreService(models.Model):
    title = models.CharField(verbose_name=u"区块标题",max_length=100,null=False,blank=False)
    en_title = models.CharField(verbose_name=u"区块英文标题",max_length=100,null=False,blank=False)
    icon = models.ImageField(verbose_name=u"图标",max_length=100,upload_to="learn/%Y/%m")
    summary = models.CharField(verbose_name=u"描述",max_length=500)
    en_summary = models.CharField(verbose_name=u"英文描述",max_length=500)
    index = models.IntegerField(verbose_name=u"顺序",default=100,blank=True)
    display = models.CharField(verbose_name=u"是否显示", max_length=1,default='1', choices=(('0', '隐藏'), ('1', '显示')))
    add_time = models.DateTimeField(verbose_name=u"上传时间",default=datetime.now)

    class Meta:
        verbose_name = u"优势与服务"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title




class Partner(models.Model):
    name = models.CharField(verbose_name=u"伙伴名称",max_length=50,null=False,blank=False)
    en_name = models.CharField(verbose_name=u"伙伴英文名称",max_length=50,null=False,blank=False)
    image = models.ImageField(verbose_name=u"图片",max_length=100,upload_to="partner/%Y/%m")
    index = models.IntegerField(verbose_name=u"顺序",default=100,blank=True)
    display = models.CharField(verbose_name=u"是否显示", max_length=1,default='1',choices=(('0', '隐藏'), ('1', '显示')))
    add_time = models.DateTimeField(verbose_name=u"上传时间",default=datetime.now)

    class Meta:
        verbose_name = u"合作伙伴"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name