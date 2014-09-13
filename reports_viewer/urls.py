from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'reports.views.all_reports'),
                       url(r'^report/(?P<report_id>\d+)/$', 'reports.views.report'),
                       )
