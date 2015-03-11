#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Datetime Module defines a function get_current_date
    and return today's day as date
    CURDATE is assigned a value none in global scope
    CURDATE is assigned today's date using the function
    get_current_date. """

import datetime
CURDATE = None


def get_current_date():
    """ Function does not take any parameters
        It returns today's day as date using
        datetime.date.today()

        Arg:
            CURDATE(date): It is assigned the value of today's date.
        Return:
            Function returns todays day as date.
    """

    today = datetime.date.today()

    return today

if __name__ == '__main__':
    CURDATE = datetime.date.today()
    print CURDATE
