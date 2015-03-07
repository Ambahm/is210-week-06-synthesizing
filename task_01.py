#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Importing datetime module - to print current date
   Conditionally executes date if it's run on command
   line.Using special variable __name__, checking how
   module is provoked. If a module’s __name__ variable
   is the string "__main__", means that the file is
   being executed as a top-level script instead of
   being imported from another file.
"""

import datetime

CURDATE = None      # settig current date as 0

# Function returns current date as date opbject

def get_current_date():
    """This function returns current date (format:YYYY,M,D).

    Args:
        Empty function
    Returns:
        str: Returns current date using date.today() class method.

    Examples:
        >>> import task_01
        >>> print task_01.CURDATE
        None

        task_01.get_current_date()
        datetime.date(2015, 3, 6)

        >>> CURDATE
        datetime.date(2015, 3, 6)
    """

    return datetime.date.today()

# executed as top-level program file, __name__ == string '__main__., at start

if __name__ == '__main__':          # Only when run
    CURDATE = get_current_date()
