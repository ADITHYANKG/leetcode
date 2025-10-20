class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        stack=[]
        result=[-1]*n
        for i in range(2*len(nums)):
            while stack and nums[i%n]>nums[stack[-1]%n]:
                index=stack.pop()
                result[index]=nums[i%n]
            stack.append(i%n)
        return result        
        