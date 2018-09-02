class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def display_list(self):
        if self.head is None:
            print("List is empty")
            return
        print("the list is:")
        p=self.head
        while p is not None:
            print(p.data,end=" ")
            p=p.next
        print()

    def insert_at_begg(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head.prev=temp
        self.head=temp

    def list_empty(self,data):
        temp=Node(data)
        self.head=temp

    def insert_at_end(self,data):
        temp=Node(data)
        p=self.head
        while p.next is not None:
            p=p.next
        p.next=temp
        temp.prev=p

    def creat(self,data):
        if self.head==None:
            self.list_empty(data)
        else:
            self.insert_at_end(data)

dl=DoubleLinkedList()
dl.creat(1)
dl.creat(10)
dl.creat(18)
dl.creat(12)
dl.creat(155)
dl.display_list()
            
