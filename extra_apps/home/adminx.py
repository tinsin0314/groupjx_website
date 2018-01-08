# -*- encoding:utf-8 -*-
__author__ = 'TINSIN'
__date__ = '2018/1/8 上午11:12'

import xadmin

from .models import Banner,LearnMoreService,Partner




class BannerAdmin(object):
    list_display = ['title','image','url','index','display','add_time']
    search_fields = ['title']
    list_filter = ['add_time','display']
    ordering = ['index']


class LearnMoreServiceAdmin(object):
    list_display = ['title','summary','index','display','add_time']
    search_fields = ['title','summary']
    list_filter = ['add_time','display']
    ordering = ['index']


class PartnerAdmin(object):
    list_display = ['name','index','display','add_time']
    search_fields = ['name']
    list_filter = ['add_time','display']
    ordering = ['index']




xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(LearnMoreService,LearnMoreServiceAdmin)
xadmin.site.register(Partner,PartnerAdmin)