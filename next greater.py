def next_greater(nums):
    """
    a=[-1]*len(n)
    for i in range(len(n)):
        for j in (n[i+1:]+n[:i]):
            #print(n[i],j,i)
            if j>n[i]:
                #print("!")
                a[i]=j
                print(a)
                break
    return a
    """
    stack = []
    output = [-1] * len(nums)
        
    for i in range(len(nums)):
        while len(stack) and nums[stack[-1]] < nums[i]:
            output[stack.pop()] = nums[i]
        stack.append(i)

    for i in range(len(nums)):
         while len(stack) and nums[stack[-1]] < nums[i]:
             if i >= stack[-1]:
                 break
             output[stack.pop()] = nums[i]
        
    return output

nums=[3,2,4,3]
print(next_greater(nums))
