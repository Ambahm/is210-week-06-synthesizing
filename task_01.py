#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using the datetime module."""

import datetime

CURDATE = None

def get_current_date():

    
    """A function using the datetime.date.today()
    to return the current day as a date object.

    Args: None given

    Return:
        To return the current date
        
    Example:    
        >>> import datetime
        >>> task_01.CURDATE
        None

        >>> task_01.get_current_date()
        datetime.date(2015, 3, 5)
        $ python -i task_01.py
        2015-03-05
    """
    return datetime.date.today()

CURDATE = get_current_date()

if __name__ == '__main__':
    print CURDATE
