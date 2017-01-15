#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SkipNode(object):
    __slots__ = ('key', 'payload', 'next', 'level', 'height')

    def __init__(self, key, level=1, payload=None):
        self.key = key
        self.payload = payload
        self.next = [None] * level

        pass

    def __str__(self):
        return "SkipNode(%s)" % self.key

class NIL(object):

    def __cmp(self, any):
        return 1

    def __str__(self):
        return 'NIL'
