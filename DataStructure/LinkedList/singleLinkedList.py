
# Singly Linked List

class Node:
    # Constructor for Linked List Node
    def __init__(self):
        self.data = None
        self.Next = None
    
    # Set Data value  for Node
    def setData(self,data):
        self.data = data
    
    # get data from the node
    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next
    
    def hasNext(self):
        return self.Next != None
    
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0
        
    def traverse(self):
        current = self.head
        count = 0
        
        while (current.next != None):
            print current.data
            count += 1
            current = current.getNext()
        
        return count
    
    def insertAtBeg(self,data):
        node = Node()
        node.setData(data)
        
        if self.length != 0:
            node.setNext(self.head)
            self.head = node
        else:
            self.head = node

        
    def insertAtEnd(self,data):
        node = Node()
        node.setData(data)
        
        current = self.head
        
        while (current.next != None):
            current = current.getNext()
        
        current.setNext(node)
        self.length += 1
        
        
    def insertAtMiddle(self,pos,data):
        if pos > self.length and pos < 0:
            return None
        if pos == 0:
            insertAtBeg(data)
        else:
            if pos == self.length:
                insertAtEnd(data)
            else:        
                node = Node()
                node.setData(data)
                current= self.head
                
                i = 0
                while(i < pos):
                    current = current.getNext()
                    i = i + 1
                    
                node.setNext(current.getNext())
                current.setNext(nnode)
            
        
        def deletefromBeg(self):
            if self.length <= 0:
                return None
            else:
                self.head = self.head.getNext()
                self.length -= 1
                
        def deletefromEnd(self):
            if self.length <= 0:
                return None
            else:
                first = self.head
                second = self.head.getNext()
                
                while(second.getNext() != None):
                    first = first.getNext()
                    second = second.getNext()
                
                first.setNext(None)
                
        def deletefromPos(self,pos):
            if pos == 0:
                deletefromBeg()
            else:
                if pos = self.length:
                    deletefromEnd()
                else:
                    first = None
                    second = self.head
                    counter = 0
                    
                    while(second != None and counter == pos -1):
                        first = second
                        second = second.getNext()
                        
                    first.setNext(second.getNext())
                    
        def delete(self):
            self.head = None

        
node1 = Node()
node2 = Node()
node1.setData(5)
node2.setData(6)
node1.setNext(node2)
print node1.getData()
    