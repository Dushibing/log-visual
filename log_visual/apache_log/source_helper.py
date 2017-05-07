#!/usr/bin/env python
# _*_encoding:utf-8_*_
"""
@version: ??
@license: Apache Licence 
@site: 
@software: PyCharm
@file: source_helper.py
@time: 27/04/17 8:22 AM
"""
__author__ = 'dushibing'

def sort_url_access_time(access_list):
    '''reutrn sort access time each url list'''
    top_10 = {}
    for item in access_list:
        top_10[(item.access_ip, item.access_url)] = top_10.get((item.access_ip, item.access_url),0)+1
    res_list = [(k[0], k[1], v) for k,v in top_10.items()]
    sort_list = sorted(res_list, key=lambda x:x[2], reverse=True)
    return sort_list

