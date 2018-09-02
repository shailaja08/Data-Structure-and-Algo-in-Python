class quTostack:
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()
    def push(self,x):
        if self.q2.size()==0:
            #print("1")
            self.q1.enqueue(x)
        else:
            self.q2.enqueue(x)


    def display(self):
        print(q1)

        
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


qu=quTostack()
qu.push(1)
qu.display()
