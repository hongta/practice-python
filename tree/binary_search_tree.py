#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tree_node import TreeNode

class BinarySearchTree:
    def __init__(self):
        self._root = None;

    def insert(self, k, payload=None):
        # tree is empty construct the tree
        if not self._root:
            self._root= TreeNode(k,payload)
        else:
            self._insert(self._root, k, payload)

    def _insert(self, tree_node, k, payload=None):
        n = TreeNode(k, payload)
        if k == tree_node.key:
            tree_node.payload = payload
            return

        if k < tree_node.key:
            if not tree_node.left:
                tree_node.left = n
            else:
                self._insert(tree_node.left, k, payload)
        else:
            if not tree_node.right:
                tree_node.right = n
            else:
                self._insert(tree_node.right, k, payload)

    def delete(self, v):
        pass

    def traverse(self):
        self._traverse(self._root)

    def _traverse(self, node):
        if node:
            if node.left:
                for n in _traverse(node.left):
                    yield n
            yield node
            if node.right:
                for n in self._traverse(node.right):
                    yield n

    def height(self):
        pass

    def search(self, v):
        pass

    def count():
        pass

if __name__ == "__main__":
    t = BinarySearchTree()
    t.insert(3)
    t.insert(8)
    t.insert(12)
    t.insert(1)
    t.insert(15)
    t.insert(7)
    print(t._root.right.left)
    # p = list(t.traverse())
    # p
    # for v in p:
    #     print v.key
