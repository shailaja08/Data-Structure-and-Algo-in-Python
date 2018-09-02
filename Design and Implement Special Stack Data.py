class stack:
    def __init__(self):
        self.st1=[]
        self.st2=[]

    def is_empty(self):
        return self.st1==None

    def push(self,val):
        self.st1.append(val)
        if self.st2==[]:
            self.st2.append(val)
        else:
            x=self.st2[-1]
            if x>val:
                self.st2.append(val)
            else:
                self.st2.append(x)

    def pop(self):
        self.st1.pop()
        self.st2.pop()

    def getMin(self):
        return self.st2[-1]

    def display(self):
        print("st1",self.st1)
        print("st2",self.st2)

st=stack()
st.push(10)
#st.display()
st.push(20)
#st.display()
st.push(30)
#st.push(16)
#st.push(15)
#st.display()
print("min",st.getMin())
st.push(5)
#st.pop()
#st.display()
print("min",st.getMin())
#st.display()

        
