# -*- coding: utf-8 -*-

class Node:
    def __init__(self,data):
        self.data = None
        self.next = None
    
    def getNext(self):
        return self.next
    
    def setNext(self.next):
        self.next = next
        
    def getData(self):
        return self.data
    
    def setData(self,data):
        self.data = data
    
    def hasNext(self):
        return self.next != None
    
    def getLength(self):
        current = self.head
        if current is None:
            return 0
        count = 1
        while(current != self.head):
            current = current.getNext()
            count = count + 1 
        return count

    def printList(self):
        current = self.head
        if current == self.head:
            return 0
        print(current.getData())
        
        while current != self.head:
            print current.getData()
            current = current.getNext()
    
    def insertAtEnd(self,data):
        current = self.head
        newNode = Node(data)
        newNode.setNext(newNode)
            
        if self.head == None:
            self.head = newNode
        else:
            while current.getNext() != self.head:
                current = current.getNext()
                
    def insertAtBeg(self,data):
        current = self.head
        newNode = Node()
        newNode.setData(data)
        
        while current.getNext() != self.head:
            current = current.getNext()
        newNode.setNext(newNode)
        
        if self.head == None:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            current.setNext(newNode)
            self.head = newNode
    
    def deleteFromLast(self):
        current = self.head
        temp = self.head
        
        if self.head == None:
            return None
        
        while(current.getNext() != self.head):
            temp = current
            current = current.getNext()
            
        temp.setNext(self.head)
    
        
    def deleteFromStart(self):
        """Delete node for the 
        the start"""
        
        if self.head == None:
            print("List is empty")
            return 
        
        current = self.head
        while current.getNext() != self.head:
            current = current.getNext()
            
        current.setNext(self.head.getNext())
        self.head = self.head.getNext()
        return



        
            
        
        
        
        
        


        
            
            
            
        
        
            
        