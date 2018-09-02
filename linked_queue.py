class QueueEmptyError(Exception):
    pass

class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size_queue=0
    def is_empty(self):
        return self.front==None
        
    def size(self):
        return self.size_queue

    def enqueue(self,data):
        temp=Node(data)
        if self.front==None:
            self.front=temp
        else:
            self.rear.next=temp
        self.rear=temp
        self.size_queue=self.size_queue+1

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyError("queue is empty")
        delete_data=self.front.data
        self.front=self.front.next
        self.size_queue=self.size_queue-1
        return delete_data

    def display(self):
        if self.is_empty():
            print("queue is empty")
            return
        print("The list is: ")
        p=self.front
        while p is not None:
            print(p.data," ",end=' ')
            p=p.next
        print()

    def peek(self):
        if self.is_empty():
            raise QueueEmptyError("queue is empty")
        return self.front.data


qu=Queue()
while True:
    print("1.enqueue")
    print("2.dequeue")
    print("3.Peek")
    print("4.Size")
    print("5.Display")
    print("6.Quit")

    choice=int(input("enter the choice:"))

    if choice==1:
        x=int(input("Enter elements to push : "))
        qu.enqueue(x)
    elif choice==2:
        print("deleted",qu.dequeue())
    elif choice==3:
        print(qu.peek())
    elif choice==4:
        print(qu.size())
    elif choice==5:
        qu.display()
    elif choice==6:
        break
    else:
        print("wrong choice")
