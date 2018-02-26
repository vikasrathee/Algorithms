# -*- coding: utf-8 -*-
class Node():
    
    def __init__(self,data=None,prev=None,next=None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def setData(self,data):
        self.data = data
    
    def getNext(self):
        return self.next
       
    def setNext(self,node):
        self.next = node
    
    def getPrev(self):
        return self.prev
    
    def setPrev(self,node):
        self.prev = node
    
    def insertAtBeg(self,data):
        node = Node(data,None,None)
        
        if self.length == 0:
            self.head = self.tail = node
        else:
            node.setPrev(None)
            node.setNext(self.head)
            self.head.setPrev(node)
            self.head = node
            
    def insertAtEnd():
        node = Node(data,None,None)
        
        if self.length == 0:
            self.head = self.tail = node
        else:
            node.setNext(None)
            node.setPrev(self.tail)
            self.tail.setNext(node)
            self.tail = node
    
    def getNode(self,index):
        currentNode = self.head
        if currentNode == None:
            return None

        counter = 0
        while(counter < index and currentNode.getNext() is not None):
            currentNode = currentNode.getNext()
            counter = counter + 1
        return currentNode    
        
    def inderAtGivenPos(self,data,pos):
        newNode = Node(data)
        
        if self.head == None pr pos == 0:
            insertAtBeg(data)
        elif pos > 0:
            temp = getNode(index)
            if temp == None or temp.getNext() == None:
                self.insert(data)
            else:
                newNode.setNext(temp.getNext())
                newNode.setPrev(temp)
                temp.setNext(newNode)
                temp.getNext.setPrev(newNode)
    
    def deleteWithData(self,data):
        temp = self.head
        while temp is not None:
            if temp.getData() == data:
                if temp.getNext() is not None:
                    temp.getNext().setNext(temp.getNext())
                    temp.getPrev().setPrev(temp.getPrev())
                else:
                    self.head = temp.getNext()
                    temp.getNext().setPrev(None)
            temp = temp.getNext()
            
            
        
                
                
                
            
            
            
        
        
        
            
        
        
        

        