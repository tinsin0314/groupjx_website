# -*- encoding:utf-8 -*-
__author__ = 'TINSIN'
__date__ = '2018/1/8 下午2:12'


from .models import Recruit

import xadmin

class RecruitAdmin(object):
    list_display = ['job_name','job_nums','index','display','add_time']
    search_fields = ['job_name']
    list_filter = ['job_nums','display','add_time']
    ordering = ['index']
    style_fields = {'job_desc':'ueditor','en_job_desc':'ueditor','requirements':'ueditor','en_requirements':'ueditor'}



xadmin.site.register(Recruit,RecruitAdmin)
