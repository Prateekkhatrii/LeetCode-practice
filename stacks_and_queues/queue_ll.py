class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None

    def push(self, x):
        newNode=Node(x)
        newNode.next=self.head
        self.head=newNode

    def pop(self):
        if self.isEmpty():
            return -1
        temp=self.head
        prev=None
        while temp.next!=None:
            prev=temp
            temp=temp.next
        x=temp.data
        if prev == None:
            self.head = None
        else:
            prev.next=None
        return x

    def peek(self):
        if self.isEmpty():
            return -1

        temp = self.head

        while temp.next != None:
            temp = temp.next

        return temp.data

    def isEmpty(self):
        return self.head is None 
