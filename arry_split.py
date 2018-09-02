def split_ar(nums,k):
    for i in range(0,k):
        x=nums[0]
        for i in range(0,len(nums)-1):
            nums[i]=nums[i+1]
        nums[-1]=x
    return nums
nums=[12, 10, 5, 6, 52, 36]
k=2
print(split_ar(nums,k))
