class QueueEmptyError(Exception):
    pass

class Queue:
    def __init__(self):
        self.items=[]
        self.front=0
        
    def is_empty(self):
        return self.front==len(self.items)

    def size(self):
        return len(self.items)-self.front

    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyError("The list is empty")
        x=self.items[self.front]
        self.items[self.front]=None
        self.front=self.front+1
        return x

    def peek(self):
        if self.is_empty():
            raise QueueEmptyError("The list is empty")
        return self.items[self.front]

    def display(self):
        print(self.items[self.front:])

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
