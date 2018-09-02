##stack using array
class EmptyStackError(Exception):
    pass

"""
class stack:
    def __init__(self):
        self.st=[]
    def isEmpty(self):
        return self.st==[]
    def size(self):
        return len(self.st)
    def push(self,val):
        self.st.append(val)
        return st
    def pop(self):
        if self.isEmpty():
            raise EmptyStackError("stack is empty")
        return self.st.pop()
    def top(self):
        if self.isEmpty():
            raise EmptyStackError("stack is empty")
        return self.st[-1]
    def display(self):
        print(self.st)
st=stack()
st.push(1)
st.display()
st.pop()
st.display()
st.push(2)
st.display()
st.push(3)
st.display()
"""
"""
###stack using LinkedList
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def size(self):
        if self.is_Empty():
            return 0
        count=0
        p=self.head
        while p:
            count+=1
            p=p.next
        return count
    
    def push(self,val):
        temp=Node(val)
        temp.next=self.head
        self.head=temp
        
    def pop(self):
        if self.isEmpty():
            raise EmptyStackError("stack is empty")
        popped_ele=self.head.data
        self.head=self.head.next
        return popped_ele
    
    def top(self):
        if self.isEmpty():
            raise EmptyStackError("stack is empty")
        return self.head.data
    def display(self):
        if self.isEmpty():
            raise EmptyStackError("stack is empty")
        p=self.head
        while p:
            print("val",p.data," ")
            p=p.next

st=stack()
st.push(1)
st.display()
print(st.pop())
#st.display()
st.push(2)
st.display()
st.push(3)
st.display()
"""
"""
#Queue using array
class Queue:
    def __init__(self):
        self.qu=[]
    def size(self):
        return len(self.qu)
    def is_Empty(self):
        return self.qu==[]
    
    def enqueue(self,val):
        self.qu.append(val)
        
    def dequeue(self):
        if self.is_Empty():
            raise EmptyStackError("stack is empty") 
        return self.qu.pop(0)
    def peek(self):
        if self.is_Empty():
            raise EmptyStackError("stack is empty") 
        return self.qu[0]
    def display(self):
        if self.is_Empty():
            raise EmptyStackError("stack is empty")
        print(self.qu)
        
        
qu=Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
qu.display()
qu.dequeue()
qu.display()
qu.dequeue()
qu.dequeue()
qu.display()
print(qu.peek())

"""
#Queue using linkedlist
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size_queue=0
    def is_Empty(self):
        return self.front==None
    def size(self):
        return self.size_queue
    
    def enqueue(self,val):
        temp=Node(val)
        if self.front ==None:
            self.front=temp
            self.rear=temp
        else:
            self.rear.next=temp
            self.rear=temp
            self.size_queue+=1
    def dequeue(self):
        if self.is_Empty():
            raise EmptyStackError("stack is empty")
        popped=self.front.data
        self.front=self.front.next
        self.size_queue-=1
        return popped
    def peek(self):
        if self.is_Empty():
            raise EmptyStackError("stack is empty")
        return self.front.data
    def display(self):
        if self.is_Empty():
            print("empty")
            return
        print("queue is")
        p=self.front
        while p:
            print(p.data)
            p=p.next

qu=Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
qu.display()
qu.dequeue()
qu.display()
qu.dequeue()
qu.dequeue()
qu.display()
print(qu.peek())
            
        
    
        
