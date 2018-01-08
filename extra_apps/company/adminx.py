# -*- encoding:utf-8 -*-
__author__ = 'TINSIN'
__date__ = '2018/1/8 下午2:32'


from .models import CompanyInfo
from xadmin import views

import xadmin


class BaseSetting(object):
    enable_themes = True   #开启主题功能
    use_bootswatch = True  #加载主题


class GlobalSettings(object):
    site_title = "激想官网后台管理系统"  #站点名称
    site_footer = "上海激想体育文化股份有限公司 版权所有 沪ICP备15052275号-2" #站点尾部
    menu_style = "accordion" #收起菜单栏


class CompanyInfoAdmin(object):
    list_display = ['name','address','tel','bd_email','market_email','hr_email']
    style_fields = {'summary':'ueditor','en_summary':'ueditor','core_business':'ueditor','en_core_business':'ueditor'}



xadmin.site.register(CompanyInfo,CompanyInfoAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)