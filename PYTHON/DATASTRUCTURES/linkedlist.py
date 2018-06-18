#!/usr/bin/python

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next

def testNode():
    node1 = Node(22)
    node2 = Node(24)
    node3 = Node(7)

    node1.next = node2
    node2.next = node3

    node1.traverse()

testNode()
