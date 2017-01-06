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
        return self._traverse(self._root)

    # Python 2 version
    def _traverse(self, node):
        if node:
            if node.left:
                for n in self._traverse(node.left):
                    yield n
            yield node
            if node.right:
                for n in self._traverse(node.right):
                    yield n


    # Python 3 version
    # def _traverse(self, node):
    #     if node:
    #         yield from self._traverse(node.left)
    #         yield node
    #         yield from self._traverse(node.right)

    def height(self):
        pass

    def search(self, k):
        return self._search(self._root, k)

    def _search(self, node, k):
        if not node:
            return None
        if k == node.key:
            return node

        if k < node.key:
            return self._search(node.left, k)
        else:
            return self._search(node.right, k)

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

    for v in t.traverse():
        print v.key

    print t.search(13)
