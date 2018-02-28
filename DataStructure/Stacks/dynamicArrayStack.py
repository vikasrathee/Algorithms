# -*- coding: utf-8 -*-
""" Implementation of *stack using dynamic arrays*
This provides a flexibility of gorwing the size of the stack on demand basis 
and we will not be faced wih challenge of stack full condition.
"""
class stack(object):
    
    # Constructor for the class
    def __init__(self, size=10):
        self.stk = [None] * size
        self.size = size
        
    # Check if stack is empty
    def isEmpty(self):
        return len(self.stk) <= 0
    
    # Push operation for the stack
    def push(self,data):
        if len(self.stk) >= self.size: 
            self.resize() 
        self.stack.append(data)
    
    # Pop operation for the stack
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return
        else:
            return self.stk.pop()
    
    def resize(self):
        newStk = list(self.stk)
        self.size = 2*self.size
        self.stk = newStk



        
        
        
    