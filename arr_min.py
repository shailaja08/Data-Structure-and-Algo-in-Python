def preprocess(arr, n):
    temp = [None] * (2 * n)
     
    # Store arr elements at i and i + n
    for i in range(n):
        temp[i] = temp[i + n] = arr[i]
    return temp
    #print(temp)
 
# Function to left rotate an array k times
def leftRotate(arr, n, k):
     
    # Starting position of array after k
    # rotations in temp will be k % n
    start = k % n
    print(start)
     
    # Print array after k rotations
    for i in range(start, start + n):
        print(arr[i%n], end = " ")
    print("")
 
# Driver program
arr = [1, 3, 5, 7, 9]
n = len(arr)
k = 2
leftRotate(arr, n, k)
k = 14
leftRotate(arr, n, k)
       

