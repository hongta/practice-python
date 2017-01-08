#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tree_node import TreeNode
from binary_search_tree import BinarySearchTree

class RedBlackTree(BinarySearchTree):
    def __init__(self):
        self._root = None;

    def left_rotate(self):
        if not self._root or not self._root.right:
            return False
        right_child = self._root.right
        self._left_rotate(self._root)
        self._root = right_child

        return True

    def left_right_rotate(self):
        if not self._root or not self._root.left or not self._root.left.right:
            return False

        return  self._left_rotate(self._root.left) and self.right_rotate()


    def right_rotate(self):
        if not self._root or not self._root.left:
            return False

        left_child = self._root.left;
        self._right_rotate(self._root)

        self._root = left_child

        return True

    def right_left_rotate(self):
        if not self._root or not self._root.right or not self._root.right.left:
            return False

        return  self._right_rotate(self._root.right) and self.left_rotate()

    def _left_rotate(self, node):
        if not node or not node.right:
            return False

        right_of_node = node.right
        self._replace_with(node, right_of_node)

        node.set_children(right=right_of_node.left)
        right_of_node.set_children(left=node)

        return True

    def _right_rotate(self, node):
        if not node or not node.left:
            return False

        left_of_node = node.left
        self._replace_with(node, left_of_node)

        node.set_children(left=left_of_node.right)
        left_of_node.set_children(right=node)

        return True

if __name__ == '__main__':
    rbt = RedBlackTree()
    rbt.insert(20)
    rbt.insert(35)
    rbt.insert(15)
    rbt.insert(40)
    rbt.insert(30)
    rbt.insert(28)
    rbt.insert(31)
    rbt.insert(17)
    rbt.insert(18)
    rbt.insert(16)
    rbt.insert(12)

    for v in rbt:
        print v
    rbt.right_left_rotate()
    print rbt._root,rbt._root.left, rbt._root.right
    # for v in rbt:
    #     print v
    # p2 = rbt.search(20)
    # print p2, p2.left, p2.right, p2.parent
