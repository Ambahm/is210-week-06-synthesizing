#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using import to create a function returning today's date."""


import datetime
CURDATE = None


def get_current_date():

    """This function will use another function to determine date.

    Args:
        It does not have any arguments.

    Returns:
        integer: date of the day it is run on.

    Examples:
        >>> task_01.get_current_date()
        datetime.date(2015, 3, 7)
    """
    return datetime.date.today()
if __name__ == '__main__':
    CURDATE = get_current_date()
