class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Circular_Linked_list:
    def __init__(self):
        self.last=None

    def display(self):
        if self.last==None:
            print("list is empty")
            return
        p=self.last.next
        while True:
            print(p.data,end=' ')
            p=p.next
            if p==self.last.next:
                break
        print()

    def insert_beg(self,data):
        temp=Node(data)
        p=self.head
        temp.next=self.last.next
        self.last.next=temp

    def insert_in_empty(self,data):
        temp=Node(data)
        self.last=temp
        self.last.next=self.last

    def insert_at_end(self,data):
        temp=Node(data)
        temp.next=self.last.next
        self.last.next=temp
        self.last=temp

    def creat(self):
        n=int(input("enter number of node"))
        if n==0:
            return
        data=int(input("enter the element"))
        self.insert_in_empty(data)
        for i in range(n-1):
            data=int(input("enter the element"))
            self.insert_at_end(data)

cl=Circular_Linked_list()
cl.creat()
cl.display()
