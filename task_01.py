#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""creating a function to return today's date"""

import datetime

CURDATE = None


def get_current_date():
    """this will give you the date.

    Args:
        none

    Returns:
        current date: returns the date

    Examples:
        >>>task_01.get_current_date()
        datetime.date(2015, 3, 9)
    """

    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
