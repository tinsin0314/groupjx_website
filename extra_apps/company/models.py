# -*- coding:utf-8 -*-
from django.db import models

from DjangoUeditor.models import UEditorField
# Create your models here.


class CompanyInfo(models.Model):
    name = models.CharField(verbose_name=u"企业名称",max_length=100,null=False,blank=False)
    en_name = models.CharField(verbose_name=u"英文企业名称",max_length=100,null=False,blank=False)
    logo = models.ImageField(verbose_name=u"企业logo",max_length=100,upload_to="companyinfo/%Y/%m")
    address = models.CharField(verbose_name=u"地址",max_length=200,null=False,blank=False)
    en_address = models.CharField(verbose_name=u"英文地址",max_length=200,null=False,blank=False)
    tel = models.CharField(verbose_name=u"联系电话",null=False,blank=False,max_length=50)
    bd_email = models.EmailField(verbose_name=u"企业合作邮箱",max_length=100)
    market_email = models.EmailField(verbose_name=u"市场推广合作邮箱",max_length=100)
    hr_email = models.EmailField(verbose_name=u"人事邮箱",max_length=100)
    summary = UEditorField(verbose_name=u'企业介绍', width=900, height=500, toolbars="full", imagePath="company/ueditor/", filePath="company/ueditor/",default="")
    en_summary = UEditorField(verbose_name=u'英文企业介绍', width=900, height=500, toolbars="full", imagePath="company/ueditor/", filePath="company/ueditor/",default="")
    core_business = UEditorField(verbose_name=u'核心业务', width=900, height=500, toolbars="full", imagePath="company/ueditor/", filePath="company/ueditor/",default="")
    en_core_business = UEditorField(verbose_name=u'英文核心业务', width=900, height=500, toolbars="full", imagePath="company/ueditor/", filePath="company/ueditor/",default="")

    class Meta:
        verbose_name = "企业信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

