#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A good module"""


import datetime


CURDATE = None


def get_current_date():
    """A date function.

    Args:
    get_current_date(): does not take any parameters.

    Returns: return the current day as a date object.

    Example:

        >>>get_current_date()
        datetime.date(2015, 3, 6)
    """
    return datetime.date.today()


if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
