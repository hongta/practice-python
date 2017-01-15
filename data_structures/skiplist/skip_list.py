#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from skip_node import SkipNode

class SkipList(object):

    def __init__(self):
        self.height = 3
        self._head = SkipNode(None, self.height, None)
        self.count = 0

    @property
    def head(self):
        return self._head


    def _update_list(self, key):
        update = [None] * self.height
        node = self.head

        for i in reversed(range(len(self.head.next))):
            while node.next[i] != None and node.next[i].key < key:
                node = node.next[i]
            update[i] = node

        return update


    def search (self, key):
        return self._search(key)

    def _search(self, key, update):
        if update == None:
            update = self._update_list(key)

        if len(update) > 0:
            candidate = update[0].next[0]
            if candidate and candidate.key == key:
                return candidate
        return None

    def insert(self, key, payload=None):
        node = SkipNode(key, self._pick_level())

        #adjust maximum height of list
        self.height = max(self.height, len(node.next))
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self._update_list(key)
        node_found = self._search(key, update)
        if node_found == None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
            self.count += 1
        else:
            #if node exists, replace payload
            node_found.payload = payload

    def delete(self, key):
        update = self._update_list(key)
        node = self._search(key, update)
        if node:
            for i in range(len(node.next)):
                update[i].next[i] = node.next[i]

                #adjust list height
                if self.head.next[i] == None:
                    self.height -= 1
            self.count -= 1

    def print_list(self):
        for i in range(len(self.head.next)-1, -1, -1):
            print "lvl ",i, ": "
            x = self.head
            lst = []
            while x.next[i] != None:
                print x.next[i].key,
                x = x.next[i]
                print ''


    def _pick_level(self):
        lvl = 1
        while random.random() < 0.5:
            lvl += 1
        return lvl
