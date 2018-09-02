def prod(nums):
    op=[]
    pro=1
    for i in range(len(nums)):
        op.append(pro)
        pro=pro*nums[i]
    print(op)
    pro=1
    for i in range(len(nums)-1,-1,-1):
        op[i]=op[i]*pro
        pro=pro*nums[i]
    print(op)

nums=[2,2,3,4]
prod(nums)
