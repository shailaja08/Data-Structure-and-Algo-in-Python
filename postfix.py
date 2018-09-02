from array_stack import Stack
def infix_to_postfix(infix):
    postfix=""
    st=Stack()
    for sym in infix:
        if sym==' ' or sym== '\t':#ignore
            continue
        if sym=='(':
            st.push(sym)
        elif sym==')':
            next=st.pop()
            while next !='(':
                postfix=postfix+next
                next=st.pop()
        elif sym in "+-*/%^":
            while not st.is_empty() and precedence(st.peek())>=precedence(sym):
                postfix=postfix+st.pop()
            st.push(sym)
        else:
            postfix=postfix+sym
    while not st.is_empty():
        postfix=postfix+st.pop()
    return postfix


def precedence(sym):
    if sym=='(':
        return 0
    elif sym in '+-':
        return 1
    elif sym in '*/%':
        return 2
    elif sym=='^':
        return 3
    else:
        return 0
#print(infix_to_postfix("1*2"))
def evaluate(postfix):
    st=Stack()
    for sym in postfix:
        if sym.isdigit():
            st.push(int(sym))
        else:
            x=st.pop()
            y=st.pop()
            if sym=='+':
                st.push(x+y)
            elif sym=='-':
                st.push(y-x)
            elif sym=='*':
                st.push(y*x)
            elif sym=='/':
                st.push(y/x)
            elif sym=='%':
                st.push(y%x)
            elif sym=='^':
                st.push(y**x)
    return st.pop()

while True:
    print("enter exp(q for quit)",end=" ")
    exp=input()
    if exp=='q':
        break
    postfix=infix_to_postfix(exp)
    print("postfix",postfix)
    print("evaluate",evaluate(postfix))
