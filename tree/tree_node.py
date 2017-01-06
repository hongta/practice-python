
class TreeNode(object):
    def __init__(self, key=None, payload=None):
        self.key = key
        self.payload = payload
        self.left = None
        self.right = None

        self.parent = None

    def __str__(self):
        s = self.key
        if self.payload:
            s += ": " + self.payload
        return str(s)
