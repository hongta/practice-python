#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tree_node import TreeNode

class BinarySearchTree:
    def __init__(self):
        self._root = None;

    def insert(self, key, payload=None):
        #1 tree is empty construct the tree
        if not self._root:
            self._root(Node(key,payload))
        else:
            self._insert(self, self._root, key, payload)

    def _insert(self, tree_node, key, payload=None):
        n = TreeNode(key, payload)
        if key < tree_node.key:
            if not tree_node.left:
                tree_node.right = n
            else:
                self._insert(self, tree_node.left, key, payload)
        else:
            if not tree_node.right:
                tree_node.right = n
            else:
                self._insert(self, tree_node.right, key, payload)

    def delete(self, v):
        pass

    def traverse(self, callback):
        pass

    def height(self):
        pass

    def search(self, v):
        pass

    def count():
        pass
