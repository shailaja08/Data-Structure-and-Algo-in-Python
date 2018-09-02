class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked:
    def __init__(self):
        self.head=None

    def insert(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
            return
        p=self.head
        while p.next is not None:
            p=p.next
        p.next=temp

    def display(self):
        p=self.head
        while p is not None:
            print(p.data)
            p=p.next
    def delete(self,value):
        p=self.head
        while p.next is not None:
            if p.next.data==value:
                p.next=p.next.next
            p=p.next
        
#Write a function to delete a Linked List
    def del_link(self):
        p=self.head
        while p is not None:
            q=p.next
            del p.data
            p=q
    def length(self):
        p=self.head
        length=0
        while p:
            length+=1
            p=p.next
        return length
    def search(self,key):
        p=self.head
        while p:
            if p.data==key:
                return True
            p=p.next
        return False
    def getnth(self,n):
        p=self.head
        count=0
        while p:
            if count==n:
                return p.data
            count+=1
            p=p.next
    def getnth_from_end(self,n):
        count=0
        p=self.head
        q=self.head
        if p is not None:
            while(count<n):
                if q is None:
                    print("n is greater than list")
                    return
                q=q.next
                count+=1
        while q:
            p=p.next
            q=q.next
        return p.data
    def reverse(self,m,n):
        q=p=self.head
        count=1
        while count<n:
            q=q.next
            count+=1
        print(count,q.data)
        count_=1
        while p:
            if count_<m:
                count_+=1
                p=p.next
            elif count_>=m:
                q.next=p.next
                count_+=1
                p=p.next
    def reverse_(self):
        p=q=self.head
        r=None
        while p:
            p=p.next
            q.next=r
            r=q
            q=p
        self.head=r
        
            
lt=Linked()
lt.insert(1)
lt.insert(2)
lt.insert(3)
lt.insert(4)
lt.insert(5)
#lt.display()
#lt.delete(5)
#lt.display()
#lt.del_link()
#print(lt.length())
#print(lt.search(5))
#print(lt.getnth(1))
#print(lt.reverse(2,4))
lt.reverse_()
lt.display()

        
            
