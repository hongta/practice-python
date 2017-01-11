#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tree_node import AVLTreeNode
from binary_search_tree import BinarySearchTree

class AVLTree(BinarySearchTree):
    def __init__(self):
        super(AVLTree, self).__init__()

    def insert(self, key):
        if not self._root:
            self._root = AVLTreeNode(key)
        else:
            self._root = self._insert(self._root, key)

    def _insert(self, node, key):
        if not node:
            return AVLTreeNode(key)

        if key < node.key:
            node.set_children(left=self._insert(node.left, key))
        elif key > node.key:
            node.set_children(right=self._insert(node.right, key))
        else:
            # duplicated key
            return node

        # 2. update height of the ancestor node
        node.height = max(self.height(node.left), self.height(node.right)) + 1

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

    def get_balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right);

    def _right_rotate(self, node):
        k1 = node.left

        self._replace_with(node, k1)

        node.set_children(left=k1.right)
        k1.set_children(right=node)

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        k1.height = max(self.height(k1.left), self.height(k1.right)) + 1

        return k1

    def _left_rotate(self, node):
        k2 = node.right

        self._replace_with(node, k2)
        node.set_children(right=k2.left)
        k2.set_children(left=node)

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        k2.height = max(self.height(k2.left), self.height(k2.right)) + 1

        return k2

if __name__ == '__main__':
    t = AVLTree()
    t.insert(10)
    t.insert(15)
    t.insert(20)
    t.insert(25)
    t.insert(30)
    p = t.search(20)
    print p, p.left, p.right, p.height, p.parent
    p = t.search(15)
    print p, p.left, p.right, p.height, p.parent
    p = t.search(25)
    print p, p.left, p.right, p.height, p.parent
