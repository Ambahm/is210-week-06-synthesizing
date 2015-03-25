#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""


import datetime
CURDATE = None


def get_current_date():
    """returns current date"""
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
