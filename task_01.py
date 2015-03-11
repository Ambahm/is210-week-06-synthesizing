#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK6 synthesizing task 01 - datetime module."""

import datetime

CURDATE = None


def get_current_date():
    """A conditional function that returns today's date.

    The conditional scope identification block will be used to identify if
    this code is being run from an imported module or directly on the command
    line.

    Args:
        None
    Returns:
        today (str) Returns today's date.
    Example:

        >>> import task_01
        >>> task_01.CURDATE
        None
        >>> task_01.get_current_date()
        datetime.date(2015, 1, 1)

        $ python -i task_01.py
        2015-01-01
        >>> CURDATE
        datetime.date(2015, 1, 1)
    """

    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
