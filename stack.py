## stack
##pop

class Stack:
    def __init__(self):
        self.st=[]

    def is_empty(self):
        return self.st==[]

    def push(self,item):
        self.st.append(item)

    def pop(self):
        if self.is_empty():
            return 0
        #x=st.pop[-1]
        #print("The pop element is",x)
        return self.st.pop()

    def size(self):
        return len(self.st)
    def peek(self):
        if self.is_empty():
            return 0
        return self.st[-1]

    def display(self):
        print(self.st)

stt=Stack()
stt.is_empty()
stt.push(8)
stt.push(2)
stt.push(21)
stt.push(23)
stt.display()
stt.pop()
stt.display()
print(stt.size())
print(stt.peek())

        
