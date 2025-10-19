class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n=len(temperatures)
        stack=[]
        result=[0]*n
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                index=stack[-1]
                result[index]=i-stack[-1]
                stack.pop()
            stack.append(i)
        return result        