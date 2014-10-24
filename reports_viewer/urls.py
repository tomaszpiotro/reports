from django.conf.urls import patterns, url
from reports.views import ReportListView, DetailReportView

urlpatterns = patterns('',
                       url(r'^$', 'reports.views.all_reports'),
                       url(r'^report/(?P<report_id>\d+)/$', 'reports.views.report'),
                       url(r'^mine/$', ReportListView.as_view(), name='my-view'),
                       url(r'^mine/(?P<report_id>\d+)/$', DetailReportView.as_view()),

                       )
