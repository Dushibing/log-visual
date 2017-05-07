from django.conf.urls import patterns, include, url
from django.contrib import admin
from apache_log.views import index, table, table2, chart, chart2
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'log_visual.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^table/$', table),
    url(r'^table2/$', table2),
                       url(r'^chart/$', chart),
                       url(r'^chart2/$',chart2),
)
