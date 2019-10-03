class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

#### craeting a stack using Linked list
class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head == None:
            self.head = Node(data)

        else:
            node = Node(data)
            node.next = self.head
            self.head = node

    def pop(self):
        if self.head == None:
            return -1
        else:
            popNode = self.head
            self.head = self.head.next
            popNode.next = None
            return popNode.data
