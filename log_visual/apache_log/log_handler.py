#!/usr/bin/env python
# _*_encoding:utf-8_*_
"""
@version: ??
@license: Apache Licence 
@site: 
@software: PyCharm
@file: log_handler.py
@time: 25/04/17 8:58 PM
"""
__author__ = 'dushibing'
import logging
from log_visual.settings import SOURCE_DIRS

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'log_visual.settings'

from apache_log.models import Access_Log, Error_Log

logger = logging.getLogger(__name__)



def split_access_log():
    res = {}
    with open(SOURCE_DIRS[0]+'/access_log/access_log') as f:
        for l in f:
            arr = l.split(' ')
            try:
            # 获取ip url 和status
                ip = arr[0]
                date = arr[3]
                url = arr[6]
                status = arr[8]
                port = arr[9]
                # ip url 和status当key，每次统计+1
                res[(ip,date,url,status,port)] = res.get((ip,date,url,status,port),0)+1
            except Exception as e:
                logger.error('index out of list')
        # 生成一个临时的list
        res_list = [(k[0],k[1],k[2],k[3],k[4],v) for k,v in res.items()]
        # 按照统计数量排序，打印前10
        for k in sorted(res_list, key=lambda x:x[3], reverse=True):
            ip = k[0]
            date = k[1][1:]
            url = k[2]
            status = k[3]
            port = k[4]
            item = Access_Log.objects.create(log_data=date, access_ip=ip, access_url=url, access_status=status, blank_field1=port)




def spilt_error_log():
    res = {}
    with open(SOURCE_DIRS[0]+'/error_log/error_log') as f:
        for l in f:
            arr = l.split('] ')
            try:
                error_date = arr[0]
                error_level = arr[1]
                error_ip = arr[2]
                error_content = arr[3]
                res[(error_date,error_level,error_ip,error_content)] = res.get((error_date, error_level, error_ip, error_content),0)+1
            except Exception as e:
                logger.error(e)
        res_list = [(k[0],k[1],k[2],k[3],v) for k,v in res.items()]
        for k in sorted(res_list, key=lambda x:x[3], reverse=True):
            print k[3]
            item = Error_Log.objects.create(error_level=k[1][1:], error_ip=k[2][8:], error_content=k[3])

