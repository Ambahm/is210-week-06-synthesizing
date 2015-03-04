#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1 module"""

import datetime

CURDATE = None


def get_current_date():
    """ A def for getting current date.

    Returns:
        datetime(string):  All arguments concatenated with commas.

    Examples:
        >>> get_current_date()
        datetime.date(2015, 3, 4)
    """
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
