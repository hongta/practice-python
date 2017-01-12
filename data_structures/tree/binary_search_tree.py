#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tree_node import TreeNode

class BinarySearchTree(object):
    def __init__(self):
        self._root = None;

    ##################
    ## Iterator method
    def __iter__(self):
        current = self._find_minmum(self._root)
        # and then, until we have reached the end:
        while current is not None:
            yield current
            # in order to get from one Node to the next one:
            current = self.successor(current)

    def _replace_with(self, old_node, new_node):
        if not old_node:
            return False

        if old_node.parent:
            if old_node.parent.left == old_node:
                old_node.parent.set_children(left=new_node)
            else:
                old_node.parent.set_children(right=new_node)
        else:
            if new_node:
                new_node.parent = None
                self._root = new_node

        return True

    def insert(self, k, payload=None):
        # tree is empty construct the tree
        if not self._root:
            self._root= TreeNode(k,payload)
        else:
            n = TreeNode(k, payload)
            self._insert(self._root, n)


    def _insert(self, tree_node, new_node):
        if new_node.key == tree_node.key:
            tree_node.payload = new_node.payload
            return tree_node

        if new_node.key < tree_node.key:
            if not tree_node.left:
                tree_node.set_children(left=new_node)
            else:
                return self._insert(tree_node.left, new_node)
        else:
            if not tree_node.right:
                tree_node.set_children(right=new_node)
            else:
                return self._insert(tree_node.right, new_node)
        return new_node

    def remove_node(self, node):
        if None:
            return
        node.key = node.payload = node.left = node.right = node.parent = None
        del node

    def delete(self, k):
        node = self.search(k)
        if not node:
            return
        p = node.parent

        if node.left and node.right:
            # if the node has two children, we replace the node's key and payload
            #  with minnum of the right substree
            min_on_right = self._find_minmum(node.right)
            min_parent = min_on_right.parent

            node.key = min_on_right.key
            node.payload = min_on_right.payload

            if min_on_right != node.right:
                #update min right child, make it become min's parent's left child
                min_parent.set_children(left=min_on_right.right)
            else:
                node.set_children(right=min_on_right.right)

            self.remove_node(min_on_right)

        else:
            # if the node has 0-1 child, we delete this node
            old_node = node
            if not node.left and not node.right:
                # no child
                node = None
            elif node.left:
                # has one left child
                node.left.parent = p
                node = node.left

            elif node.right:
                # has one right child
                node.right.parent = p
                node = node.right

            if not p:
                #trying to delete root node
                self._root = node
            else:
                if p.left == old_node:
                    p.left = node
                else:
                    p.right = node
            self.remove_node(old_node)

    def find_minnum(self):
        return self._find_minmum(self._root)

    def _find_minmum(self, node):

        if not node:
            return None

        while node.left:
            node = node.left
        return node

    def find_maxmum(self):
        return self._find_maxmum(self._root)

    def _find_maxmum(self, node):
        if not node:
            return None

        while node.right:
            node = node.right
        return node

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

    def successor(self, node):
        if not node:
            return None

        if node.right:
            return self._find_minmum(node.right)

        p = node.parent
        while p and p.right == node:
            node = p
            p = p.parent
        return p

    def predecessor(self, node):
        if not node:
            return None

        if node.left:
            return self._find_maxmum(node.left)

        p = node.parent
        while p and p.left == node:
            node = p
            p = p.parent
        return p

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
    # t.insert(3)
    # t.insert(8)
    # t.insert(12)
    # t.insert(1)
    # t.insert(15)
    # t.insert(7)
    data = [30, 25, 49, 35, 68, 33, 34, 38, 40, 37, 36]
    for i in data:
        t.insert(i)
    for v in t.traverse():
        print v.key
    d = t._find_maxmum(t._root)
    while d:
        print d.key
        d = t.successor(d)
