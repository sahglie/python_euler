#! /usr/bin/env python

import sys


JAN, FEB, MAR, APR, MAY, JUNE, JULY, AUG, SEPT, OCT, NOV, DEC = range(1, 13)
MON, TUES, WED, THURS, FRI, SAT, SUN = range(1, 8)

def number_of_sundays():
    """1 Jan 1900 was a Monday.
    How many Sundays fell on the first of the month during the twentieth 
    century (1 Jan 1901 to 31 Dec 2000)?
    """
    sundays = 0
    for date in date_iterator():
        month, day, year, day_of_week = date
        if day_of_week == SUN and day == 1 and year != 1900:
            sundays += 1
    return sundays

def date_iterator():
    day_of_week = 1
    for year in range(1900, 2001):
        for month in range(1, 13):
            for day in range(1, days_in_month(month, year)+1):
                yield [month, day, year, day_of_week]
                if day_of_week >= 7:
                    day_of_week = 1
                else:
                    day_of_week += 1

def is_leap_year(year):
    """A leap year occurs on any year evenly divisible by 4, but not 
    on a century unless it is divisible by 400
    """
    is_century = lambda a_year: a_year % 100 == 0
    if is_century(year):
        return year % 400 == 0 and year % 4 == 0
    else:
        return year % 4 == 0

def days_in_month(month, year):
    days_lookup = {
        JAN: 31, FEB: feb_days(year), MAR: 31,
        APR: 30, MAY: 31, JUNE: 30, 
        JULY: 31, AUG: 31, SEPT: 30, 
        OCT: 31, NOV: 30, DEC: 31,
        }
    return days_lookup[month]

def feb_days(year):
    if is_leap_year(year):
        return 29 
    else:
        return 28


if "__main__" == __name__:
    print number_of_sundays()
