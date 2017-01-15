#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SkipNode(object):
    __slots__ = ('key', 'payload', 'next', 'level')

    def __init__(self, key, level=1, payload=None):
        self.key = key
        self.payload = payload
        self.next = [None] * level

        pass

    def __str__(self):
        return "SkipNode(%s)" % self.key
