import random
def pick(nums,target=3):
        """
        :type target: int
        :rtype: int
        """
        dic={}
        for key,val in enumerate(nums):
            if val in dic:
                #print("2")
                dic[val].append(key)
                #print(dic)
            else:
                #print("21")
                dic[val]=[key]
                #print(dic)
        for v in dic.keys():
            if v==target:
                print(random.choice(dic[v]))
                return

nums=[1,2,3,3,3]
pick(nums)
