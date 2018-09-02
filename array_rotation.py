def arr_rotate(arr,d,n):
    temp=arr[0:d]
    for i in range(0,n-d):
        arr[i]=arr[i+d]
    arr[n-d:]=temp[0:]
    #arr[n-d+1]=temp[1]
    return arr
                                    

d=2
arr=[1,2,3,4,5,6,7]
n=len(arr)
print(arr_rotate(arr,d,n))
