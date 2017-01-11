#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tree_node import AVLTreeNode
from binary_search_tree import BinarySearchTree

class AVLTree(BinarySearchTree):
    def __init__(self):
        pass

    def insert(self, key):
        if not self._root:
            self._root = AVLTreeNode(key)
        else:
            self._root = self._insert(key, self._root)

    def _insert(self, node, key):
        if not node:
            return AVLTreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            # duplicated key
            return node

        # 2. update height of the ancestor node
        node.height = get_max_height(node.left, node.right) + 1

        # 3. check whether the node became unbalanced
        balance = self.get_balance(node)
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def height(self, n):
        if not n:
            return 0
        else:
            return n.height

    def get_balance(node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right);

    def get_max_height(self, x, y):
        if x is None:
            x_height = 0
        else:
            x_height = x.height

        if y is None:
            y_height = 0
        else:
            y_height = y.height

        return max(x_height, y_height)

    def _right_rotate(self, node):
        k1 = node.left

        self._replace_with(node, k1)

        node.set_children(left=k1.right)
        k1.set_children(right=node)

        node.height = self.get_max_height(node.right, node.left) + 1
        k1.height = self.get_max_height(k1.left, k1.right) + 1

        return k1

    def _left_rotate(self, node):
        k2 = node.right

        self._replace_with(node, k2)
        node.set_children(right=k2.left)
        k2.set_children(left=node)

        node.height = self.get_max_height(node.left, node.right) + 1
        k2.height = self.get_max_height(k2.left, k2.right) + 1

        return k2
