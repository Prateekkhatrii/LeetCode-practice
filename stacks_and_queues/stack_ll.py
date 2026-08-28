class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedListStack:
    def __init__(self):
        self.head=None

    def push(self, x):
        newNode=Node(x)
        newNode.next=self.head
        self.head=newNode

    def pop(self):
        if self.isEmpty():
            return -1
        x=self.head.data
        self.head=self.head.next
        return x

    def top(self):
        if self.isEmpty():
            return -1
        return self.head.data
    def isEmpty(self):
        return self.head is None 
