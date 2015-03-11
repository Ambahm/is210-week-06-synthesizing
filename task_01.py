#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""

import datetime

CURDATE = None


def get_current_date():
    """Return current day as date object

    Args:
        (int): Currnet day
    Returns:
        date: 'Know what I mean?' followed by Arg wink and 'nudge ' set number
             of times
    Example:

        >>> get_current_date()
        datetime.date(2015, 3, 8)
    """
    return datetime.date.today()


if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
