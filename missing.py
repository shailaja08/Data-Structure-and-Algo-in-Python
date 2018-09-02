def abc(num):
    i=1
    x=[]
    while i <= len(num):
        if i not in num:
            #print("true")
            x.append(i)
        i+=1
        #print(i)
    return x

num=[4,3,2,7,8,2,3,1]
print(abc(num))
