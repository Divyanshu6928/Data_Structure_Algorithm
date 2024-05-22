class Node:
    def __init__(self,data,next=None) :
        self.data=data
        self.next=next

class Stack:
    def __init__(self):
        self.sz=0
        self.head=None

    def size(self):
        return self.sz
    
    def is_empty(self):
        return self.size()==0
    
    def push(self,element):
        newNode =Node(element,self.head)
        self.head=newNode
        self.sz+=1

    def pop(self):
        if self.is_empty():
            raise Exception ("Stack Underflow")
        temp = self.head                    # to delete this node 
        data = temp.data                    # to return popped data

        self.head=self.head.next            # 
        del temp
        return data
    
    def top(self):
        if self.is_empty():
            raise Exception ("Stack Underflow")
        return self.head.data
    
    def __str__(self):
        el=[]

        trav = self.head
        while trav:
            el.append(str(trav.data))
            trav=trav.next

        return '->'.join(el)
    
st=Stack()
st.push(2)
st.push(4)
st.push(6)
print(st.size())
print(st)
print("Top-->",st.top())

st.pop()
print("After popping 6 \n",st)
