import time
start_time=time.time()
class Node(object):
    def __init__(self, data):
        self.data=data
        self.nextNode = None
		
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    def insetbegin(self,data):
	newNode = Node(data)
	newNode.next = self.head
	self.head = newNode
    def insertEnd(self,data):
        self.size=self.size+1
        newNode=Node(data)
        
        actualNode=self.head
        
        if not self.head:
            self.head=newNode
        else:
            while actualNode.nextNode is not None:
                actualNode=actualNode.nextNode
            actualNode.nextNode=newNode
    def groupreverse(self,k):
        currentNode=self.head
        start=None
        last=None
        actualNode=None
        while currentNode:
            previous=None
            actualNode=currentNode
            count=1
            while (currentNode and count <= k):
                    next=currentNode.nextNode
                    currentNode.nextNode=previous
                    previous=currentNode
                    currentNode=next
                    count=count+1
            if start is None:
                start=previous
            if last is not None:
                last.nextNode=previous
            last=actualNode

        while start is not None:
            print(start.data,end=" ")
            start=start.nextNode


linkedlist=LinkedList()

linkedlist.insertEnd(1)
linkedlist.insertEnd(2)
linkedlist.insertEnd(3)
linkedlist.insertEnd(4)
linkedlist.insertEnd(5)
linkedlist.insertEnd(6)




linkedlist.groupreverse(4)



print()
print(time.time()-start_time)
                

