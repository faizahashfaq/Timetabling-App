import django_tables2 as tables
from Activity_Scheduler.models import *


class timetable(tables.Table):
    class Meta:
        model = Timetable