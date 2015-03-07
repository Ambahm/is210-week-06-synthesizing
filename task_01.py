#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" week 6 sys task_0 module"""


import datetime


CURDATE = None


def get_current_date():
    """ A function to return current date.

    Returns:
        datetime(date): return current day as a date.

    Examples:
        >>> get_current_date()
       datetime.date(2015, 3, 6)

       >>> task_01.get_current_date()
       datetime.date(2015, 1, 1)
    """

    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
