#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import Random
import sys
import os
sys.path.append(os.path.join('..', 'data_structures'))
from skiplist.skip_list import SkipList
from skiplist.skip_node import SkipNode


class TestSkipList(unittest.TestCase):

    def setUp(self):
        self.sl = SkipList()

    def test_empty(self):
        self.assertEqual(self.sl.count, 0)
        self.assertEqual(self.sl.height, 3)
        for i in self.sl.head.next:
            self.assertEqual(i, None)

    # Test Insertion

    def test_insert_in_asc_order(self):
        self.sl.insert(1)
        self.sl.insert(2)
        self.sl.insert(3)
        self.sl.insert(4)
        p = self.sl.head.next[0]
        self.assertEqual(p.key, 1)
        p = p.next[0]
        self.assertEqual(p.key, 2)
        p = p.next[0]
        self.assertEqual(p.key, 3)
        p = p.next[0]
        self.assertEqual(p.key, 4)
        if self.sl.head.next[1]:
            self.assertIn(self.sl.head.next[1].key, [1,2,3,4])
        if self.sl.head.next[2]:
            self.assertIn(self.sl.head.next[1].key, [1,2,3,4])

    def test_insert_in_desc_order(self):
        self.sl.insert(4)
        self.sl.insert(3)
        self.sl.insert(2)
        self.sl.insert(1)
        p = self.sl.head.next[0]
        self.assertEqual(p.key, 1)
        p = p.next[0]
        self.assertEqual(p.key, 2)
        p = p.next[0]
        self.assertEqual(p.key, 3)
        p = p.next[0]
        self.assertEqual(p.key, 4)
        if self.sl.head.next[1]:
            self.assertIn(self.sl.head.next[1].key, [1,2,3,4])

        if self.sl.head.next[2]:
            self.assertIn(self.sl.head.next[1].key, [1,2,3,4])

    def test_insert_in_unorder(self):
        self.sl.insert(1)
        self.sl.insert(3)
        self.sl.insert(4)
        self.sl.insert(2)
        p = self.sl.head.next[0]
        self.assertEqual(p.key, 1)
        p = p.next[0]
        self.assertEqual(p.key, 2)
        p = p.next[0]
        self.assertEqual(p.key, 3)
        p = p.next[0]
        self.assertEqual(p.key, 4)
        if self.sl.head.next[1]:
            self.assertIn(self.sl.head.next[1].key, [1,2,3,4])
        if self.sl.head.next[2]:
            self.assertIn(self.sl.head.next[1].key, [1,2,3,4])

    def test_insert_same_key(self):
        self.sl.insert(1)
        self.sl.insert(3)
        self.sl.insert(4)
        self.sl.insert(2)
        self.sl.insert(3)
        self.assertEqual(self.sl.count, 4)
        p = self.sl.head.next[0]
        self.assertEqual(p.key, 1)
        p = p.next[0]
        self.assertEqual(p.key, 2)
        p = p.next[0]
        self.assertEqual(p.key, 3)
        p = p.next[0]
        self.assertEqual(p.key, 4)
        if self.sl.head.next[1]:
            self.assertIn(self.sl.head.next[1].key, [1,2,3,4])
        if self.sl.head.next[2]:
            self.assertIn(self.sl.head.next[1].key, [1,2,3,4])

    # Test Deletion

    def test_delete_in_list(self):
        self.sl.insert(1)
        self.sl.insert(3)
        self.sl.insert(4)
        self.assertEqual(self.sl.count, 3)
        self.sl.delete(1)
        self.assertEqual(self.sl.count, 2)

    def test_delete_not_in_list(self):
        self.sl.insert(1)
        self.sl.insert(3)
        self.sl.insert(4)
        self.assertEqual(self.sl.count, 3)
        self.sl.delete(5)
        self.assertEqual(self.sl.count, 3)

    def test_delete_to_empty(self):
        self.sl.insert(1)
        self.sl.insert(7)
        self.sl.insert(4)
        self.sl.delete(1)
        self.sl.delete(4)
        self.sl.delete(7)
        self.assertEqual(self.sl.count, 0)



    # Test Search
    def test_search_in_empty(self):
        self.assertIsNone(self.sl.search(13))
        self.sl.insert(12)
        self.sl.insert(3)
        self.sl.delete(3)
        self.sl.delete(12)
        self.assertIsNone(self.sl.search(3))
        self.assertIsNone(self.sl.search(12))
        self.assertEqual(self.sl.count, 0)

    def test_search(self):
        self.sl.insert(1)
        self.sl.insert(3)
        self.sl.insert(4)
        self.sl.insert(2)
        self.assertEqual(self.sl.search(1).key, 1)
        self.assertEqual(self.sl.search(4).key, 4)
        self.assertEqual(self.sl.search(2).key, 2)
        self.sl.delete(2)
        self.assertIsNone(self.sl.search(2))

    # Test Magic functions

    def test_magic_len(self):
        self.sl.insert(1)
        self.sl.insert(3)
        self.sl.insert(4)
        self.assertEqual(len(self.sl), 3)

    def test_magic_set_and_get_item(self):
        self.sl[12] = "abc"
        self.sl[8] = "abcdd"
        self.sl[9] = "dd"
        self.sl[28] = "abcwc"
        self.sl.insert(13, "123")

        self.assertIsNotNone(self.sl.search(12))
        self.assertEqual(self.sl.search(8).payload, "abcdd")
        self.assertEqual(self.sl[9], "dd")
        self.assertEqual(self.sl[13], "123")

        self.sl[13]= "abcd"
        self.assertEqual(self.sl[13], "abcd")
        self.sl.delete(13)

        with self.assertRaises(KeyError):
            self.sl[13]

    def tearDown(self):
        self.sl = None


# if __name__ == '__main__':
#     unittest.main()
