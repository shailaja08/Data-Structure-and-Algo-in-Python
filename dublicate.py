def x(num,k):
    dic={}
    for i in num:
        if i+k in num:
            dic[i+k]=1
        else:dic[i+k]=0
    print (dic)
    for key,value in dic.items():
        if dic[key]==1:
            return True
    return False

num=[1,5,8,9,15]
#dic={8:1,12:0,15:1}
print(x(num,7))
