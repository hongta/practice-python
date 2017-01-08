#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tree_node import TreeNode
from binary_search_tree import BinarySearchTree

class RedBlackTree(BinarySearchTree):
    def __init__(self):
        self._root = None;

    def rotate_left(self):
        if not self._root or not self._root.right:
            return False

        old_root = self._root
        new_root = old_root.right
        new_root.parent = None

        old_root.set_children(right=new_root.left)
        new_root.set_children(left=old_root)

        self._root = new_root

        return True

    def rotate_left_grandson(self):
        if not self._root or not self._root.right or not self._root.right.left:
            return False

        old_root = self._root
        old_root_right = old_root.right
        new_root = old_root.right.left
        new_root.parent = None

        old_root.set_children(right=new_root.left)
        old_root_right.set_children(left=new_root.right)
        new_root.set_children(left=old_root, right=old_root_right)

        self._root = new_root

        return True

    def rotate_right(self):
        if not self._root or not self._root.left:
            return False

        old_root = self._root
        new_root = old_root.left
        new_root.parent = None

        old_root.set_children(left=new_root.right)
        new_root.set_children(right=old_root)

        self._root = new_root

        return True

    def rotate_right_grandson(self):
        if not self._root or not self._root.left or not self._root.left.right:
            return False

        old_root = self._root
        old_root_right = old_root.left
        new_root = old_root.left.right
        new_root.parent = None

        old_root.set_children(left=new_root.right)
        old_root_right.set_children(right=new_root.left)
        new_root.set_children(left=old_root_right, right=old_root)

        self._root = new_root

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
    # rbt.rotate_left_grandson()
    rbt.rotate_right_grandson()
