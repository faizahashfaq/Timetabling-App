from django import template

from Activity_Scheduler.Functions import *
from Activity_Scheduler.forms import *

register = template.Library()


@register.simple_tag(name='keyValueName')
def keyValueName(value: TimeSlot, i, j, k):
    """

    :type value: object
    """
    try:
        tm = TimeSlot.objects.get(day=i, period=j, section=k)
        if tm.course is None:
            return 'Empty'
        return tm.course.name
    except TimeSlot.DoesNotExist:
        return 'Empty'


@register.simple_tag(name='keyValueTe')
def keyValueTe(value: TimeSlot, i, j, k):
    """

    :type value: object
    """

    try:
        tm = TimeSlot.objects.get(day=i, period=j, section=k)
        if tm.course is None:
            return 'Empty'
        return tm.teacher
    except TimeSlot.DoesNotExist:
        return 'Empty'


@register.simple_tag(name='keyValueR')
def keyValueR(value: TimeSlot, i, j, k):
    """

    :type value: object
    """

    try:
        tm = TimeSlot.objects.get(day=i, period=j, section=k)
        if tm.course is None:
            return 'Empty'
        return 'Room# '+str(tm.room)
    except TimeSlot.DoesNotExist:
        return 'Empty'


@register.filter(name='times')
def times(number):
    try:
        return range(0, number)
    except:
        return []
