#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from binary_search_tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.tree = BinarySearchTree()

    def runTest(self):
        pass

    def tearDown(self):
        self.tree = None

if __name__ == '__main__':
    unittest.main()
