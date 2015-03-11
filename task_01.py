#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Module for Today's Date"""

import datetime

CURDATE = None


def get_current_date():
    """Returns the current date.

    Args:
        ' ' (empty): no arg is needed.

    Returns:
        str: The current date in year, month, day format.

    Examples:

        >>>get_cur_date()
        datetime.date(2015, 3, 7)

    """
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
