##Selection Sort

def selection_sort(num):
    for i in range(len(num)-1):
        minIndex=i
        for j in range(i+1,len(num)):
            if num[j]<num[minIndex]:
                minIndex=j
        if i!=minIndex:
            num[minIndex],num[i]=num[i],num[minIndex]
            #print(num)
    return num
## Bubble_Sort
def bubble_sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
    return num

def improved_bubble_sort(num):
    for i in range(len(num)-1,0,-1):
        swap=0
        for j in range(i):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
                swap+=1
        if swap==0:
            break
    return num
#Insertion_sort
def insertion_sort(num):
    for i in range(1,len(num)):
        temp=num[i]
        j=i-1
        while j>=0 and num[j]>temp:
            num[j+1]=num[j]
            j=j-1
        num[j+1]=temp
    return num
num=[1,4,2,8,0]
print(selection_sort(num))
print(bubble_sort(num))
print(insertion_sort(num))
