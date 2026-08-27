#implement stack using array
class ArrayStack:
    def __init__(self):
        self.stack=[]

    def push(self, x):
        self.stack.append(x)
 
    def pop(self):
        if self.isEmpty():
            return -1
        return self.stack.pop()

    def top(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]
     
    def isEmpty(self):
        return len(self.stack)==0
