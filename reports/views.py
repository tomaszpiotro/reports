from django.shortcuts import render_to_response
from django.db.models import Count
from reports.models import Report
from reports.models import Reports_fitemsets
from reports.models import FreqItemsets
from reports.models import PrevOccurrences
import itertools
from graphos.renderers.highcharts import LineChart
from graphos.sources.simple import SimpleDataSource



def all_reports(request):
    rep = Report.objects.all().order_by('id').reverse()
    reports_list = []
    for r in rep:
        reports_list.append((r, Reports_fitemsets.objects.filter(report_id=r.id).count()))
    return render_to_response('reports.html', {'reports': reports_list})


def report(request, report_id=1):
    reportt = Report.objects.get(id=report_id)
    reports_fitemsets = Reports_fitemsets.objects.filter(report_id=report_id)
    fitemsets = []
    for f in reports_fitemsets:
        fitemsets.append(FreqItemsets.objects.get(id=f.fitemset_id))
    occurrences = PrevOccurrences.objects.filter(report=report_id)
    sets = []
    for f in fitemsets:
        sets.append((f, occurrences.filter(freq_itemset_id=f.id).count()))
    sets.sort(key=lambda tup: tup[0].remote_host)
    sets.sort(key=lambda tup: tup[1], reverse=True)
    grouped = itertools.groupby(occurrences, lambda record: record.date.strftime("%Y-%m-%d"))
    occurrences_by_day = [(day, len(list(occurrences_this_day))) for day, occurrences_this_day in grouped]
    occurrences_by_day.insert(0, ('date', 'occurrences'))
    print occurrences_by_day.__len__()
    asd = occurrences_by_day[:50]
    wykr = LineChart(SimpleDataSource(data=asd), html_id="bar_chart")

    return render_to_response('report.html', {'report': reportt, 'reports_fitemsets': sets, 'report_id': report_id, 'chart': wykr})

