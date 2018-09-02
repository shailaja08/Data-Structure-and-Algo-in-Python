class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None

    def insert_end(self,data):
        temp=Node(data)
        if self.head is None:
            self.head=temp
            return
        p=self.head
        while p.next is not None:
            p=p.next
        p.next=temp

    def creat_list(self):
        n=int(input("enter the number of nodes"))
        
        if n==0:
            print("empty list")
            return
        for i in range(n):
            data=int(input("enter the element :"))
            self.insert_end(data)

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

    def bubble_sort_exchange_data(self):
        end=None
        
        while end!=self.head.next:
            p=self.head
            while p.next!=end:
                q=p.next
                if p.data >q.data:
                    p.data,q.data=q.data,p.data
                p=p.next
            end=p

    def count(self):
        p=self.head
        count=0
        while p is not None:
            count=count+1
            p=p.next
        return count

    def getCountRec(self, node):
        if (not node): # Base case
            return 0
        else:
            return 1 + self.getCountRec(node.next)
 
    # A wrapper over getCountRec()
    def getCount(self):
       return self.getCountRec(self.head)

    def search(self,key):
        p=self.head
        if self.head==None:
            return False
        while p is not None:
            if p.data==key:
                return True
            p=p.next
        return False

    def search_rec(self,node,key):
        if node==None:
            return False
        elif node.data==key:
            return True
        else:
            return self.search_rec(node.next,key)
        
        


    def search_main(self,key):
        return self.search_rec(self.head,key)
        


ll=Linked_list()
ll.creat_list()
ll.display()
#print(ll.getCount())
#print(ll.search_main(50))
