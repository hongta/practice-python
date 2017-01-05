#!/usr/bin/env python
# -*- coding: utf-8 -*-

#http://codereview.stackexchange.com/questions/114435/python-linked-list
#https://github.com/jwasham/practice-python/blob/master/linked_lists/node.py

from node import Node

class UnorderedList(object):

    def __init__(self):
        self.head = None

    ##################
    ## Iterator method
    # def __iter__(self):
    #     current = self.head
    #     # and then, until we have reached the end:
    #     while current is not None:
    #         yield current
    #         # in order to get from one Node to the next one:
    #         current = current.next

    ##################
    ## Iterator method
    ## http://stackoverflow.com/questions/28316668/python-linked-list-with-nodes-iterable
    # def next(self):
    #     current = self.head
    #     # and then, until we have reached the end:
    #     while current is not None:
    #         yield current
    #         # in order to get from one Node to the next one:
    #         current = current.next


    #################
    ## Supports index operator
    def __getitem__(self, key):
        if isinstance(key, slice):
            pass
        else:
            pass
        pass

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            pass
        else:
            pass
        pass

    def __delitem__(self, key):
        if isinstance(key, slice):
            pass
        else:
            pass
        pass



    #same as add
    def prepend(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def size(self):
        cur = self.head
        count = 0

        while cur:
            count += 1
            cur = cur.next
        return count

    def search(self, data):
        cur = self.head

        while cur:
            if cur.data == data:
                return True
            cur = cur.next

        return False

    def delete(self, data):
        cur = self.head
        prev = None
        while cur:
            if cur.data == data:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            prev = cur
            cur = cur.next

        return False

    def append(self, data):
        n = Node(data)
        if  self.head:
            self.head = n
        else:
            iter_node = self.head
            while iter_node.next:
                iter_node = iter_node.next
            iter_node.next = n

    def insert(self, postion, data):
        if postion < 0:
            raise IndexError("Index out of bounds");

        if postion == 0:
            self.add(data)
            return

        cur = self.head
        _pos = 1
        new_node = Node(data)

        while cur:
            if postion == _pos:
                new_node.next = cur.next
                cur.next = new_node
                return True
            _pos += 1
            cur = cur.next

        if not cur:
            raise IndexError("Index out of bounds");

    def reverse(self):
        cur = self.head
        prev = None

        while cur:
            _next = cur.next
            cur.next = prev
            prev = cur
            cur = _next
        self.head = prev


    def pop(self, index):
        pass

    def __str__(self):
        cur = self.head
        out = ['Head']
        while cur:
            out.append(cur.data)
            cur = cur.next
        return "->".join(map(str,out))

def testUnorderedList():
    data = [10, 23, 12,49]
    ul = UnorderedList()
    ul.prepend(10)
    ul.prepend(23)
    print(ul.size())
    ul.prepend(13)
    ul.prepend(33)
    print ul
    ul.insert(1, 99)
    print(ul)
    # print(ul)
    ul.reverse()
    print(ul)
    # for v in ul:
    #     print(v)
    # print ul.delete(13)



if __name__ == "__main__":
    testUnorderedList()
