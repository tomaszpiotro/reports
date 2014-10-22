from django.db import models

# Create your models here.


class Report(models.Model):
    date = models.DateTimeField()
    interval = models.IntegerField()

    class Meta:
        db_table = u'reports'


class Operations(models.Model):
    id = models.IntegerField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    minsup = models.SmallIntegerField()
    interval = models.IntegerField()
    request_id = models.IntegerField()
    tag = models.CharField(max_length=32)

    class Meta:
        db_table = u'operations'


class FreqItemsets(models.Model):
    oid = models.ForeignKey(Operations,db_column='oid')
    protocol = models.CharField(max_length=32)
    remote_host = models.IPAddressField()
    remote_port = models.IntegerField()
    local_host = models.IPAddressField()
    local_port = models.IntegerField()
    count = models.IntegerField()
    generator = models.BooleanField(default=False)
    jep = models.BooleanField(db_column='ejp', default=False)
    interesting = models.BooleanField(db_column='interesting', default=False)

    class Meta:
        db_table = u'freq_itemsets'


class ReportsFitemsets(models.Model):
    report = models.ForeignKey(Report)
    fitemset = models.OneToOneField(FreqItemsets)
    same_without_protocol = models.IntegerField()
    same_without_remote_host = models.IntegerField()
    same_without_remote_port = models.IntegerField()
    same_without_local_port = models.IntegerField()
    same_without_count = models.IntegerField()
    same_without_interesting = models.IntegerField()

    class Meta:
        db_table = u'reports_fitemsets'


class PrevOccurrences(models.Model):
    report = models.OneToOneField(Report, primary_key=True, db_column='report_id')
    freq_itemset = models.OneToOneField(FreqItemsets, primary_key=True, db_column='freq_itemset_id')
    date = models.DateTimeField()

    class Meta:
        db_table = u'prev_occurrences'