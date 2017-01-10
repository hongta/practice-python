#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tree_node import TreeNode, RedBlackTreeNode
from binary_search_tree import BinarySearchTree

class RedBlackTree(BinarySearchTree):
    def __init__(self):
        super(RedBlackTree, self).__init__()

    def insert(self, k, payload=None):
        # tree is empty construct the tree
        new_node = RedBlackTreeNode(k,payload)
        if not self._root:
            self._root= new_node
            node = new_node
        else:
            new_node = self._insert(self._root, new_node)

        self._insert_fixup(new_node)

    def _insert_fixup(self, x):

        while x.parent and x.parent.color == "red":
            if x.uncle and x.uncle.color == "red":
                """
                                   x
                                  / \
                                 R   R
                                    / \
                                   x   g
                """
                x.parent.color = "black"
                x.parent.parent.color = "red"
                x.uncle.color = "red"
                x = x.parent.parent
            else : # uncle is "black"
                if x.parent == x.parent.parent.left:
                    if x == x.parent.right:
                        """
                                   .
                                  / \
                                 R   B
                                / \
                               .   x
                        """
                        x = x.parent
                        self._left_rotate(x)
                    x.parent.color = "black"
                    x.parent.parent.color = "red"
                    self._right_rotate(x.parent.parent)
                else:
                    if x == x.parent.left:
                        """
                               .
                              / \
                             B   R
                                / \
                               x   .
                        """
                        x = x.parent
                        self._right_rotate(x)
                    x.parent.color = "black"
                    x.parent.parent.color = "red"
                    self._right_rotate(x.parent.parent)

        self._root.color = "black"

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
        """Left-rotates node x on tree T.

                   x
                  / \
                 a   y
                    / \
                   b   g

            mutates into:

                       y
                      / \
                     x   g
                    / \
                   a   b

        Used for maintaining tree balance.
        """
        if not node or not node.right:
            return False

        right_of_node = node.right
        self._replace_with(node, right_of_node)

        node.set_children(right=right_of_node.left)
        right_of_node.set_children(left=node)

        return True

    def _right_rotate(self, node):
        """Right-rotates node x on tree T.

                   x
                  / \
                 y   g
                / \
               a   b

        mutates into:

                   y
                  / \
                 a   x
                    / \
                   b   g

        Used for maintaining tree balance.
        """
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
    # rbt.insert(12)
    # rbt.insert(35)

    for v in rbt:
        print v,v.color
    rbt.insert(12)
    for v in rbt:
        print v,v.color
    rbt.right_left_rotate()
    print rbt._root,rbt._root.left, rbt._root.right

    p = RedBlackTreeNode(25,"abc")
    print p.key, p.payload
    # for v in rbt:
    #     print v
    # p2 = rbt.search(20)
    # print p2, p2.left, p2.right, p2.parent
