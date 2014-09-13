#!/usr/bin/env python

import psycopg2
import datetime

type_str = type('str')
type_datetime = type(datetime.datetime.now())
type_int = type(1)
type_float = type(1.0)
type_None = type(None)


def convert2str(record):
    res = []
    for item in record:
        if type(item) == type_None:
            res.append('NULL')
        elif type(item) == type_str:
            res.append("'"+item+"'")
        elif type(item) == type_datetime:
            res.append("'"+str(item)+"'")
        else:  # for numeric values
            res.append(str(item))
    result = ','.join(res)
    print result
    return result


def copy_table(source_table_name, dest_table_name):
    conn1 = psycopg2.connect(database="miner_copy", user="postgres", password="qwerty1asd", host="localhost")
    cur1 = conn1.cursor()

    conn2 = psycopg2.connect(database="miner", user="miner", password="minerminer", host="xp1.zoak.ii.pw.edu.pl")
    cur2 = conn2.cursor()

    cur1.execute("SELECT max(id) FROM %s;" % dest_table_name)
    max_id = cur1.fetchone()[0]
    if max_id is None:
        max_id = 0
        print "None"

    cur2.execute("SELECT * FROM %s where id > %s;" % (source_table_name, max_id.__str__()))
    for row in cur2.fetchall():
        val_str = convert2str(row)
        print str(tuple(row))
        cur1.execute("INSERT INTO %s VALUES (%s)" % (dest_table_name, val_str))

    conn2.commit()
    cur2.close()
    conn2.close()
    conn1.commit()
    cur1.close()
    conn1.close()


copy_table("operations", "operations")
copy_table("freq_itemsets", "freq_itemsets")