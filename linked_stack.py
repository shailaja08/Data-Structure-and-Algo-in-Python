class EmptyStackError(Exception):
    pass
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def is_empty(self):
        return self.top==None

    def size(self):
        if self.is_empty():
            return 0
        count=0
        p=self.top
        while p is not None:
            count+=1
            p=p.next
        return count

    def push(self,data):
        temp=Node(data)
        temp.next=self.top
        self.top=temp
        
    def reverse(self):
        prev=None
        p=self.top
        while p is not None:
            q=p.next
            p.next=prev
            prev=p
            p=q
        self.top=prev

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("stack is empty")
        popped_element=self.top.data
        self.top=self.top.next
        return popped_element

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("stack is empty")
        return self.top.data

    def display(self):
        p=self.top
        while p is not None:
            print(p.data,end=" ")
            p=p.next
        print()

st=Stack()
while True:
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Size")
    print("5.Display")
    print("6.Reverse")
    print("7.Quit")

    choice=int(input("enter the choice:"))

    if choice==1:
        x=int(input("Enter elements to push : "))
        st.push(x)
    elif choice==2:
        print("popped element",st.pop())
    elif choice==3:
        print(st.peek())
    elif choice==4:
        print(st.size())
    elif choice==5:
        st.display()
    elif choice==6:
        st.reverse()
    elif choice==7:
        break
    else:
        print("wrong choice")
