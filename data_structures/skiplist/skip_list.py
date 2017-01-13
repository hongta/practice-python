#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from itertools import dropwhile, count, cycle
from skip_node import SkipNode, NIL

class SkipList(object):

    def __init__(self):
        self._head = None
        self._tail = SkipNode(NIL())
        self._height = 10
        pass

    def _pick_level(self):
        lvl = 1
        while random.random() < 0.5 and lvl < self._height:
            lvl += 1
        return lvl


    def _geometric(self, p):
        return (next(dropwhile(lambda _: random.randint(1, int(1. / p)) == 1, count())) for _ in cycle([1]))


if __name__ == '__main__':
    s = SkipList()
    print s._pick_level()
    print s._pick_level()
    print s._pick_level()
    print s._pick_level()
