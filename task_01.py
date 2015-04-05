#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Importing datetime module -Using special variable __name__"""

import datetime
CURDATE = None      # settig current date as 0


# Function returns current date as date opbject

def get_current_date():
    """This function returns current date format YYYY,M,D.

    Args:
        Empty function

    Returns:
        datetime(date): Returns current date using date.today() class method.

    Examples:
        >>> get_current_date()
        datetime.date(2015, 3, 31)

        task_01.get_current_date()
        datetime.date(2015, 3, 6)

    """

    return datetime.date.today()



if __name__ == '__main__':          # Only when run
    # executed as top-level program file, __name__ == string '__main__ at start

    CURDATE = get_current_date()
    print CURDATE
