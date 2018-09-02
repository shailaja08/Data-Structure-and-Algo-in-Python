class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Single_linkedlist:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("The list is an empty list")
        else:
            print("The list is:  ")
        p=self.head
        while p is not None:
            print(p.data,end=" ")
            p=p.next
        print()
        
    def size(self):
        n=0
        p=self.head
        while p is not None:
            n=n+1
            p=p.next
        print(n)
        if n==0:
            print("The list is empty with the size",n)

    def search(self,x):
        position=1
        p=self.head
        while p is not None:
            if p.data==x:
                print("the position of the element is ",position)
                return True
            position=position+1
            p=p.next
        else:
            print("The element is not found")
            return False

    def insert_in_beginning(self,data): # also work for empty list
        temp=Node(data)
        temp.next=self.head
        self.head=temp

    def insert_in_end(self,data):
        temp=Node(data)
        if self.head is None:
            self.head=temp
            return
        p=self.head
        while p.next is not None:
            p=p.next
        p.next=temp

    def creat_list(self):
        n=int(input("enter no. of node:"))
        if n==0:
            return
        for i in range(n):
            data=int(input("enter the value"))
            self.insert_in_end(data)
        
    def delete_first_node(self):
        p=self.head
        self.head=p.next
    def delete_only_node(self):
        p=self.head
        self.head=None
        
    def delete_from_between(self,data):
        p=self.head
        while p.next is not None:
            if p.next.data==data:
                p.next=p.next.next
            p=p.next     
"""
        if p.next is None:
            print(data,"is not in the list")
        else:
            p=p.next.next

    def delete_from_end(self):
        p=self.head
        while p.next.next is not None:
            p=p.next
        p.next=None

    def reverse(self):
        prev=None
        p=self.head
        while p is not None:
            next=p.next
            p.next=prev
            prev=p
            p=next
        self.head=prev
            

    def bubble_sort(self):
        end=None
        while end!=self.head.next:
            p=self.head
            while p.next!=end:
                q=p.next
                if p.data>q.data:
                    p.data,q.data=q.data,p.data
                p=p.next
            end=p

    def getnth(self,k):
        count=0
        p=self.head
        while p.next is not None:
            
            if count==k:
                print("the value if ",p.data)
                return
            count=count+1
            p=p.next

    def getnth_rec(self,p,k):
        count=1
        #p=self.head
        if count==k:
            print(node.data)
        else:
            self.getnth_rec(self.next,k-1)
    def remove_dublicate(self):
        p=self.head
        while p is not None:
            q=p.next
            while q is not None:
                if p.data==q.data:
                    p.next=q.next
                q=q.next
            p=p.next
                
"""             

ll=Single_linkedlist()
ll.creat_list()
ll.display()
ll.delete_from_between(1)
ll.display()
