#!/usr/bin/env python
# _*_ coding:utf-8 _*_

__author__ = 'Domon'

'''
Database operation module.
'''

import time
import uuid
import functools
import threading
import logging

# Dict object:


class Dict(dict):


    '''
    Simple dict but support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y'] 
    200
    >>> d2 = Dict(a=1, b=2,c = '3')
    >>> d2.c
    '3'
    >>> d2['empty']
        Traceback (most recent call last):
            ...
        KeyError: 'empty'
        >>> d2.empty
        Traceback (most recent call last):
            ...
        AttributeError: 'Dict' object has no attribute 'empty'
        >>> d3 = Dict(('a', 'b', 'c'), (1, 2, 3))
        >>> d3.a
        1
        >>> d3.b
        2
        >>> d3.c
        3
    '''
