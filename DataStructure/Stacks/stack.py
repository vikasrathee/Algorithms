# -*- coding: utf-8 -*-

class Stack:
    
    def __init__(self,size = 10):
        self.stk = []
        self.size = size
    
    def push(self,data):
        if len(self.stk) < self.size:
            self.stk.append(data)
            print "Stack after push",self.stk
        else:
            print "Stack is full"     
    
    def isEmpty(self):
        return len(self.stk) <= 0
    
    def pop(self):
        if self.isEmpty():
            print "Stack is empty"
        else:
            self.stk.pop()
            print "Stack after push",self.stk
        

stack = Stack(10)
stack.isEmpty()
stack.push(10)
stack.push(12)
stack.push(13)
stack.push(10)
stack.push(12)
stack.push(13)
stack.push(10)
stack.push(12)
stack.push(13)
stack.push(10)
stack.push(12)
stack.push(13)
print(stack.pop())

        
        
