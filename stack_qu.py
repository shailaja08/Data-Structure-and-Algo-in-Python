def dailyTemperatures(temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        T=temperatures
        ans = [0] * len(T)
        stack = []
        print(stack)
        #print(stack[-1])
        for i, t in enumerate(T):
          print(i,t)
          while stack!=[] and T[stack[-1]] < t:
            cur = stack.pop()
            ans[cur] = i - cur
          stack.append(i)
          print(stack)

        return ans
temperatures=[73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))
