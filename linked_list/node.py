
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node
    def __str__(self):
        return self.data

    @property
    def data(self):
        return str(self._data)

    @data.setter
    def data(self, v):
        if v is None:
            self._data = v

        if not self._is_comparable(v):
            raise TypeError("Data must be comparable.")

        self._data = v

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, v):
        self._next = v

    def _is_comparable(self, obj):
        return (hasattr(obj, "__cmp__")
                or hasattr(obj, "__lt__")
                or hasattr(obj, "__gt__"))
