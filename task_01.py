#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1"""


import datetime

CURDATE = None


def get_current_date():
    """Getting the current date.

    Args:
    get_current_date(): take no parameters.
    
    Returns:
    return the current date object.

    Example:
        >>>get_current_date()
        datetime.date(2015, 3, 8)
    """
    return datetime.date.today()


if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
