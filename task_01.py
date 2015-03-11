#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring"""

import datetime

CURDATE = None


def get_current_date():
    """ Explaining the function get_current_date

    Args:
        Gets the current date

    Returns:
        Returns the current date

    Examples:
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

if __name__ == "__main__":
    CURDATE = get_current_date()
    print CURDATE
