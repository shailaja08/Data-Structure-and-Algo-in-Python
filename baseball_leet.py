#["5","2","C","D","+"]
def baseball(arr):
    st=[]
    num=0
    sum_=0
    for i in range(len(arr)):
        #print(type(int(arr[i])))
        if arr[i] in ["0","1","2","3","4","5","6","7","8","9","-2"]:
            st.append(int(arr[i]))
            sum_=sum_+int(arr[i])
            #print(st)
            #print("sum",sum_)

        elif arr[i]=="C":
            #st.append("invaid")
            sum_=sum_-st.pop()
            #print(st)
            #print("sum",sum_)

        elif arr[i]=="D":
            popped=st.pop()
            st.append(popped)
            st.append(2*popped)
            sum_=sum_+2*popped
            #print(st)
            #print("sum",sum_)

        elif arr[i]=="+":
            popped_1=st.pop()
            popped_2=st.pop()
            num=popped_1+popped_2
            st.append(popped_2)
            st.append(popped_1)
            st.append(num)
            sum_=sum_+num
            #print(st)
            #print("sum",sum_)

    #print(sum_)
    return sum_

arr=["5","-2","4","C","D","9","+","+"]
baseball(arr)
