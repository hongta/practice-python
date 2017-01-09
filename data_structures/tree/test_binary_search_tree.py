#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from random import Random
from binary_search_tree import BinarySearchTree
from tree_node import TreeNode


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):

        #tree 1
        self.tree = BinarySearchTree()
        random = Random(283)
        self.data = set([random.randint(1,1000) for i in xrange(100)])
        for v in self.data:
            self.tree.insert(v)

        #tree 2
        self.tree2 = BinarySearchTree()
        self.tree2.insert(20)
        self.tree2.insert(45)
        self.tree2.insert(12)

    def test_key_attributes(self):
        root = self.tree2._root
        node_12 = root.left
        node_45 = root.right
        self.assertIsInstance(root, TreeNode)
        self.assertEqual(root.left.key, 12)
        self.assertEqual(root.right.key, 45)
        self.assertEqual(root.parent, None)


        self.assertEqual(node_12.left, None)
        self.assertEqual(node_12.right, None)
        self.assertEqual(node_12.parent.key, 20)

        self.assertEqual(node_45.left, None)
        self.assertEqual(node_45.right, None)
        self.assertEqual(node_45.parent.key, 20)

    def test_insert(self):
        self.tree2.insert(15)
        node_15 = self.tree2._root.left.right
        self.assertEqual(node_15.left, None)
        self.assertEqual(node_15.right, None)
        self.assertEqual(node_15.parent.key, 12)
        pass

    def tearDown(self):
        self.tree = None
        self.tree2 = None

if __name__ == '__main__':
    unittest.main()
