"""
class stackToqueue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def is_empty(self):
        return self.s1==[]
    def qu_enque(self,x):
        return self.s1.append(x)
    def qu_deque(self):
        while self.s1!=[]:
            popped_element=self.s1.pop()
            #print(popped_element)
            self.s2.append(popped_element)
            #print(self.s2)
        return self.s2.pop()

    def display(self):
        print(self.s1)

sq=stackToqueue()
sq.qu_enque(1)
sq.qu_enque(2)
sq.qu_enque(3)
sq.qu_enque(4)
sq.display()
sq.qu_deque()
sq.qu_enque(5)
#sq.display()
"""

class queueTostack:
    def __init__(self):
        self.qu1=Queue()
        self.qu2=Queue()
    def is_empty(self):
        if self.qu1==[] and self.qu2==[]:
            return
    def push(self,x):
        if self.qu1==[] and self.qu2==[]:
            self.qu1.enqueue(x)
            print(1)
        elif self.qu1==[] and self.qu2!=[]:
            self.qu2.enqueue(x)
        elif self.qu2==[] and self.qu1!=[]:
            self.qu1.enqueue(x)
        
    def pop(self):
        if self.qu1==[] and self.qu2==[]:
            return
        elif self.qu2==[] and self. qu1!=[]:
            front=0
            rear=len(self.qu1)
            while(front!=rear):
                popped=self.qu1.dequeue()
                self.qu2.enqueue(popped)
                front+=1
            return self.qu1.dequeue()
        elif self.qu1==[] and self.qu2!=[]:
            front=0
            rear=len(self.qu1)
            while(front!=rear):
                popped=self.qu2.dequeue()
                self.qu1.enqueue(popped)
                front+=1
            return self.qu2.dequeue()
        
    def display(self):
        if self.qu2==[] and self.qu1!=[]:
            print(self.qu1)
        #print(self.qu2)
        elif self.qu1==[] and self.qu2!=[]:
            print(self.qu2)

class QueueEmptyError(Exception):
    pass

class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyError("The list is empty")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise QueueEmptyError("The list is empty")
        return self.items[0]

    def display(self):
        print(self.items)

qs=queueTostack()
qs.push(1)
qs.push(2)
qs.push(3)
qs.display()
qs.pop()
qs.display()
