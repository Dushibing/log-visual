#coding:utf-8
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from . import models
from source_helper import sort_url_access_time

def index(request):

    return render(request, 'index.html', locals())


def table(request):
    access_list = models.Access_Log.objects.all()
    top = sort_url_access_time(access_list)
    return render(request, 'table.html', {"top_10":top[:10]})


def table2(request):
    access_list = models.Access_Log.objects.all()
    top_sort = sort_url_access_time(access_list)
    paginator = Paginator(top_sort, 8)
    page = request.GET.get('page')
    try:
        last = paginator.page(page)
    except PageNotAnInteger:
        last = paginator.page(1)
    except EmptyPage:
        last = paginator.page(paginator.num_pages)
    print last
    return render(request, 'table2.html', {"top_sort": last})

def chart(request):
    access_list = models.Access_Log.objects.all()
    ip_sort = dict()
    date_sort = dict()
    for item in access_list:
        if item.access_ip not in ip_sort:
            ip_sort[item.access_ip] = 0
        else:
            ip_sort[item.access_ip] += 1
    value_sort = sorted(ip_sort.items(), key=lambda d: d[1], reverse=True)
    for item in access_list:
        if item.log_data.split(':')[0] not in date_sort:
            date_sort[item.log_data.split(':')[0]] = 0
            print date_sort
        else:
            date_sort[item.log_data.split(':')[0]] += 1
    access_date = sorted(date_sort.items(), key=lambda d: d[1])
    return render(request, 'chart.html', {"top_10": value_sort[:5], 'access_date':access_date})


def chart2(request):
    """because don't has enough real source data for the map chart, so dowmload the json data from internet,
    weibo source data,if has really data you need handler if on here
    """
    #这里如果是IP数据需要实际去确认每个IP的地理位置信息，由于无法找到一份全国的访问IP数据，所以我直接使用了地理位置信息
    return render(request, 'chart2.html')