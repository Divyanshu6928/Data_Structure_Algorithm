class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

    def __str__(self):
        return str(self.data)

class DLL:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    
    def append(self,data):         #append something end of that
        newNode = Node(data)
        if self.isEmpty():
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.next = newNode
            newNode.prev = self.__tail
            self.__tail=newNode

        self.__size +=1


    def addFirst(self,data):
        newNode=Node(data)
        if self.isEmpty():
            self.__head = newNode
            self.__tail = newNode
        else:
            newNode.next=self.__head
            self.__head.prev=newNode
            self.__head=newNode
        
        self.__size+=1

    def addAt(self,index,data):
        if index < 0 or index > self.size():
            raise Exception("Invalid Index")
        if index == 0:
            self.addFirst(data)
        elif index==l.size():
            self.append(data)
        else:
            id=0
            trav=self.__head
            while id != index-1:
                id+=1
                trav=trav.next
            newNode=Node(data,trav,trav.next)
            trav.next=newNode
            newNode.next.prev=newNode
            self.__size+=1
                

    def removeFirst(self):
        if self.isEmpty():
            raise Exception ("Can't remove")
        else:
            temp=self.__head
            self.__head=self.__head.next
            self.__head.prev=None
            del temp
        self.__size-=1

    def removeLast(self):
        if self.isEmpty():
            raise Exception ("Can't remove")
        else:
            temp=self.__tail
            self.__tail=self.__tail.prev
            self.__tail.next=None
            del temp
        self.__size-=1

    def removeAt(self,index):


        i=0
        trav=self.__head

        while i!=index-1:
            i+=1
            trav=trav.next
            

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.size()==0
        
    # def Contain(self,element):

    # def indexof(self,element):

    def __str__(self):
        l=[]
        trav=self.__head
        while trav is not None:
            l.append(trav.data)
            trav = trav.next

        return ' <---> '.join(map(str,l))


l=DLL()

l.append(43)
l.append(23)
l.append(12)
l.append(45)
l.addAt(2,40)
l.addAt(4,56)
l.addFirst(67)
l.removeFirst()
l.removeLast()
print(l.size())
print(l)