import datetime
import itertools
from types import Occurrences

from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404

from reports.models import Report
from reports.models import ReportsFitemsets
from reports.models import FreqItemsets
from reports.models import PrevOccurrences


def all_reports(request):
    rep = Report.objects.all().order_by('-date')
    reports_list = []
    for r in rep:
        reports_list.append((r, ReportsFitemsets.objects.filter(report_id=r.id).count(),
                             r.date+datetime.timedelta(hours=r.interval)))
    paginator = Paginator(reports_list, 100)
    page = request.GET.get('page')
    try:
        reports = paginator.page(page)
    except PageNotAnInteger:
        reports = paginator.page(1)
    except EmptyPage:
        reports = paginator.page(paginator.num_pages)
    return render_to_response('reports.html', {'reports': reports})


def report(request, report_id=1):
    reportt = get_object_or_404(Report, id=report_id)
    reports_fitemsets = ReportsFitemsets.objects.filter(report_id=report_id)
    fitemsets = []
    for f in reports_fitemsets:
        fitemsets.append(FreqItemsets.objects.using('miner').get(id=f.fitemset_id))
    occurrences = PrevOccurrences.objects.filter(report=report_id)
    sets = []
    occurrences_map = {}
    for f in fitemsets:
        sets.append((f, occurrences.filter(freq_itemset_id=f.id).count(), reports_fitemsets.get(fitemset_id=f.id)))
        grouped = itertools.groupby(occurrences.filter(freq_itemset_id=f.id), lambda record: record.date.strftime("%Y-%m-%d"))
        occurrences_by_day = [(day, len(list(occurrences_this_day))) for day, occurrences_this_day in grouped]
        occurrences_map.update({f.id: Occurrences(occurrences_by_day)})
    sets.sort(key=lambda tup: tup[0].remote_host)
    sets.sort(key=lambda tup: tup[1], reverse=True)

    end_date = reportt.date + datetime.timedelta(hours=reportt.interval)
    return render_to_response('report.html', {'report': reportt, 'reports_fitemsets': sets,
                                              'occurrences': occurrences_map, 'end_date': end_date})

