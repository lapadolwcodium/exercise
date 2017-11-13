from calendar import day_name
from datetime import date, timedelta

starts_of_date = {
    '1st': 1,
    '2nd': 8,
    '3rd': 15,
    '4th': 22,
    '5th': 29,
    'teenth': 13,
}


def is_leap_year(year):
    is_leap = False

    if year % 4 == 0:
        is_leap = True

    if year % 400 == 0:
        is_leap = True

    if year % 4 == 0 and year % 100 != 0:
        is_leap = True

    if year % 100 == 0 and year % 400 != 0:
        is_leap = False

    return is_leap


def last_day_start(year, month):
    return ([25, 22 + int(is_leap_year(year))] + [25, 24, 25, 24, 25] * 2)[month - 1]


def meetup_day(year, month, day_of_the_week, which):
    start = date(year, month, starts_of_date.get(which, last_day_start(year, month)))
    offset_date = list(day_name).index(day_of_the_week) - start.weekday()
    return start + timedelta(days=offset_date % 7)
