from array_stack import Stack
class getmin:
    def get_min(self,nums):#16 15 18
        st_1=Stack()
        st_2=Stack()
        if st_1.is_empty() and st_2.is_empty():#16 15 18  15
            st_1.push(nums)
            st_2.push(nums)
        else:
            st_1.push(nums)
            if nums<st_2[0]:
                st_2.pop()
                st_2.push(nums)
        x=st_2.pop()
        return x
gt=getmin()
while True:
    print("enter value",end=" ")
    exp=int(input())
    if exp==0:
        break
    else:print(gt.get_min(exp))
    #print("evaluate",evaluate(postfix))
