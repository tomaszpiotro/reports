import time
import datetime
from datetime import timedelta


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)+1):
        yield start_date + timedelta(n)


class Occurrences():
    def __init__(self, start_date, end_date, data):
        self.start_date = start_date
        self.end_date = end_date
        self.data = data

    def __init__(self, occurrences):
        self.data = self.occurrences_to_day_list(occurrences)

    def occurrences_to_day_list(self, occurrences_by_day):
        occurrences_by_day.sort(key=lambda tup: tup[0])
        occurrences = []
        if occurrences_by_day.__len__() > 0:
            self.start_date = datetime.datetime.strptime(occurrences_by_day[0][0], '%Y-%m-%d').date()
            self.end_date = datetime.datetime.strptime(occurrences_by_day[-1][0], '%Y-%m-%d').date()
            dates_only = [i[0] for i in occurrences_by_day]
            for single_date in daterange(self.start_date, self.end_date):
                date = time.strftime("%Y-%m-%d", single_date.timetuple())
                if date in dates_only:
                    index = dates_only.index(date)
                    occurrences.append(occurrences_by_day[index][1])
                else:
                    occurrences.append(0)
        return occurrences
