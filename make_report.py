#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
import datetime
from datetime import timedelta


def remove_index_from_tuple(t, index):
    lst = list(t)
    lst.__delitem__(index)
    return tuple(lst)


def tuple_evaluate(t):
    lst = list(t)
    for i in range(lst.__len__()):
        if lst[i] is None:
            lst[i] = "is NULL"
        else:
            if isinstance(lst[i], str):
                lst[i] = "= '" + lst[i].__str__() + "'"
            else:
                lst[i] = "= " + lst[i].__str__()
    return remove_index_from_tuple(tuple(lst), 0)


interval = 10
print "running report script. Hours: " + interval.__str__()

conn1 = psycopg2.connect(database="miner_copy", user="postgres", password="qwerty1asd", host="localhost")
cur1 = conn1.cursor()

conn2 = psycopg2.connect(database="miner_copy", user="postgres", password="qwerty1asd", host="localhost")
cur2 = conn1.cursor()

conn3 = psycopg2.connect(database="miner_copy", user="postgres", password="qwerty1asd", host="localhost")
cur3 = conn1.cursor()

now = datetime.datetime.now()
min_time = now - timedelta(hours=interval)

cur1.execute("select f.id, f.protocol, f.remote_host, f.remote_port, f.local_port, f.count, f.interesting "
             "from freq_itemsets as f, operations as o where f.oid = o.id and o.end_time > timestamp ' %s '" % min_time)

insert_string = "insert into reports (date, interval) values (%s, %s) returning id"
cur2.execute(insert_string, (now, interval))
inserted_report_id = cur2.fetchone()[0]

for row in cur1.fetchall():
    evaluated_row = tuple_evaluate(row)
    insert_values = remove_index_from_tuple(evaluated_row, 0)
    cur2.execute("select count(*) from freq_itemsets where remote_host %s and remote_port %s and local_port %s and count %s and interesting %s" % insert_values)
    same_without_protocol = cur2.fetchone()[0]
    insert_values = remove_index_from_tuple(evaluated_row, 1)
    cur2.execute("select count(*) from freq_itemsets where protocol %s and remote_port %s and local_port %s and count %s and interesting %s " % insert_values)
    same_without_remote_host = cur2.fetchone()[0]
    insert_values = remove_index_from_tuple(evaluated_row, 2)
    cur2.execute("select count(*) from freq_itemsets where protocol %s and remote_host %s and local_port %s and count %s and interesting %s " % insert_values)
    same_without_remote_port = cur2.fetchone()[0]
    insert_values = remove_index_from_tuple(evaluated_row, 3)
    cur2.execute("select count(*) from freq_itemsets where protocol %s and remote_host %s and remote_port %s and count %s and interesting %s" % insert_values)
    same_without_local_port = cur2.fetchone()[0]
    insert_values = remove_index_from_tuple(evaluated_row, 4)
    cur2.execute("select count(*) from freq_itemsets where protocol %s and remote_host %s and remote_port %s and local_port %s and interesting %s" % insert_values)
    same_without_count = cur2.fetchone()[0]
    insert_values = remove_index_from_tuple(evaluated_row, 5)
    cur2.execute("select count(*) from freq_itemsets where protocol %s and remote_host %s and remote_port %s and local_port %s and count %s" % insert_values)
    same_without_interesting = cur2.fetchone()[0]

    final_values = (inserted_report_id, row[0], same_without_protocol, same_without_remote_host, same_without_remote_port, same_without_local_port, same_without_count, same_without_interesting)
    cur2.execute("insert into reports_fitemsets (report_id, fitemset_id, same_without_protocol, same_without_remote_host, same_without_remote_port, same_without_local_port, same_without_count, "
                 "same_without_interesting) values(%s, %s, %s, %s, %s, %s, %s, %s)" % final_values)


cur1.execute("select f.id, f.protocol, f.remote_host, f.remote_port, f.local_host, f.local_port, f.count "
             "from freq_itemsets as f, operations as o where f.oid = o.id and o.end_time > timestamp ' %s '" % min_time)
for row in cur1.fetchall():
    sel = "select o.start_time from operations as o, freq_itemsets as f where f.oid = o.id and f.protocol %s and f.remote_host %s and f.remote_port %s and f.local_host %s and f.local_port %s and f.count %s and o.start_time < timestamp ' %s ' " % (tuple_evaluate(row) + (min_time,))
    cur2.execute(sel)
    for date in cur2.fetchall():
        ins = "insert into prev_occurrences (report_id, freq_itemset_id, date) values (%s, %s, %s)"
        cur3.execute(ins, (inserted_report_id, row[0], date))

conn1.commit()
cur1.close()
conn1.close()

conn2.commit()
cur2.close()
conn2.close()

conn3.commit()
cur3.close()
conn3.close()
