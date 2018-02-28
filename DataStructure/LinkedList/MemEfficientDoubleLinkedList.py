# -*- coding: utf-8 -*-

class NewNode:
    def __init__(self):
        self.data = None
        self.ptrdiff = None
        
    def setdata(self,data):
        self.data = data
    
    def getData(self):
        return self.data

    ## Uses the exclusive or operation
    def setPtr(self,prev,next):
        self.ptrdiff = prev ^ next
    