
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
