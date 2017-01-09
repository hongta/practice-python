#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TreeNode(object):
    def __init__(self, key=None, payload=None):
        self.key = key
        self.payload = payload
        self.left = None
        self.right = None

        self.parent = None

    def __str__(self):
        s = str(self.key)
        if self.payload:
            s += ": " + str(self.payload)
        return s

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, v):
        if v is None:
            self._left = v
            return

        if not isinstance(v, TreeNode):
            raise TypeError("The instance type should be TreeNode")

        self._left = v

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, v):
        if v is None:
            self._right = v
            return

        if not isinstance(v, TreeNode):
            raise TypeError("The instance type should be TreeNode")

        self._right = v

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, v):
        if v is None:
            self._parent = v
            return

        if not isinstance(v, TreeNode):
            raise TypeError("The instance type should be TreeNode")

        self._parent = v

    def set_children(self, **kwargs):
        """
            This funciton used to set node's children, and also update its parent
            Usage:
            node1.set_children(left=node2)
            node1.set_children(right=node3)
            node1.set_children(left=node2, right=node3)
        """
        old_children = (self.left, self.right)
        if "left" in kwargs:
            self.left = kwargs["left"]
            if self.left:
                self.left.parent = self

        if "right" in kwargs:
            self.right = kwargs["right"]
            if self.right:
                self.right.parent = self

        return old_children

class RedBlackTreeNode(TreeNode):

    def __init__(self, key=None, payload=None):
        super(RedBlackTreeNode,self).__init__(key, payload)
        self.color="red"

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, v):
        if v and v in ["red", "black"]:
            self._color = v
        else:
            raise ValueError("The value for color only allow 'red' or 'black'.")
