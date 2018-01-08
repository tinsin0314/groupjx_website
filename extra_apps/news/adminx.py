# -*- encoding:utf-8 -*-
__author__ = 'TINSIN'
__date__ = '2018/1/8 下午1:20'


from .models import Category,News

import xadmin

class CategoryAdmin(object):
    list_display = ['name','index','display','add_time']
    search_fields = ['name']
    list_filter = ['display']
    ordering = ['index']



class NewsAdmin(object):
    list_display = ['title','category','author','summary','display','add_time']
    search_fields = ['title','author']
    list_filter = ['category__name','display','add_time']
    ordering = ['add_time']
    style_fields ={'content':'ueditor','en_content':'ueditor'}

xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(News,NewsAdmin)