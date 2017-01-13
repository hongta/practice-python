#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SkipNode(object):
    __slots__ = ('key', 'payload', 'next', 'down', 'height')

    def __init__(self, key, payload=None):
        self.key = key
        self.payload = payload
        
        pass

class NIL(object):

    def __cmp(self, any):
        return 1

    def __str__(self):
        return 'NIL'
