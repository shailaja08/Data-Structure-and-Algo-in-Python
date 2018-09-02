def dublicate(arr,k):
    s=[]
    for i in range(len(arr)):
        if arr[i] in s:
            return True
        s.append(arr[i])
        #print("i",i)
        #print(s)
        if i>=k:
            s.pop(0)
            #print("s",s)
    return False
k=2
arr=[1,2,3,2,1,2,3,4]
print(dublicate(arr,k))
