class EmptyStackError(Exception):
    pass

class FullStackError(Exception):
    pass
class Stack:
    def __init__(self,max_size=10):
        self.items=[None]*max_size
        self.count=0
    def is_empty(self):
        return self.count==0

    def is_full(self):
        return self.count==len(self.items)

    def size(self):
        return self.count

    def push(self,item):
        if self.is_full():
            return FullStackError("Stack is full")
        self.items[self.count]=x
        self.count+=1

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        x=self.items[self.count-1]
        self.items[self.count-1]=None
        self.count-=1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.items[self.count-1]

    def display(self):
        print(self.items)


st=Stack()
while True:
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Size")
    print("5.Display")
    print("6.Quit")

    choice=int(input("enter the choice:"))

    if choice==1:
        x=int(input("Enter elements to push : "))
        st.push(x)
    elif choice==2:
        print("popped",st.pop())
    elif choice==3:
        print(st.peek())
    elif choice==4:
        print(st.size())
    elif choice==5:
        st.display()
    elif choice==6:
        break
    else:
        print("wrong choice")
        
    
               
        
    
