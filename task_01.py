#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module that returns actual date"""
import datetime

CURDATE = None


def get_current_date():
    """Return the date today"""
    return datetime.date.today()


if __name__ == '__main__':
    CURDATE = get_current_date()
