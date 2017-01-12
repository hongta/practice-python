#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tree_node import AVLTreeNode
from binary_search_tree import BinarySearchTree

class AVLTree(BinarySearchTree):
    def __init__(self):
        super(AVLTree, self).__init__()

    def insert(self, k, payload=None):
        # tree is empty construct the tree
        if not self._root:
            self._root= AVLTreeNode(k,payload)
        else:
            n = AVLTreeNode(k, payload)
            self._insert(self._root, n)

    def _insert(self, tree_node, new_node):
        if new_node.key == tree_node.key:
            tree_node.payload = new_node.payload
            return tree_node

        if new_node.key < tree_node.key:
            if not tree_node.left:
                tree_node.set_children(left=new_node)
            else:
                self._insert(tree_node.left, new_node)
        else:
            if not tree_node.right:
                tree_node.set_children(right=new_node)
            else:
                self._insert(tree_node.right, new_node)

        return self._avl_insert_fixup(tree_node)


    def _avl_insert_fixup(self, node):

        # 2. update height of the ancestor node
        self._update_height(node)

        # 3. check whether the node became unbalanced
        balance = self.get_balance(node)
        print balance
        if self.get_balance(node) ==2:
            print "node.right: ", self.get_balance(node.right)
            if self.get_balance(node.right) < 0:
                node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        if self.get_balance == -2:
            print "node.left: ", self.get_balance(node.left)
            if self.get_balance(node.left) > 0:
                node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        return node

    def _update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        
    def height(self, n):
        if not n:
            return 0
        else:
            return n.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.height(node.right) - self.height(node.left);

    def _right_rotate(self, node):
        k1 = node.left

        self._replace_with(node, k1)

        node.set_children(left=k1.right)
        k1.set_children(right=node)

        self._update_height(node)
        self._update_height(k1)

        return k1

    def _left_rotate(self, node):
        k2 = node.right

        self._replace_with(node, k2)
        node.set_children(right=k2.left)
        k2.set_children(left=node)

        self._update_height(node)
        self._update_height(k2)

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
