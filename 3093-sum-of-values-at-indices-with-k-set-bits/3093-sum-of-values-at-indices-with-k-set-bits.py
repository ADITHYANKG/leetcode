class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        
        for i in range(len(nums)):
            b=bin(i)
            s=str(b)
            n=s.count("1")
            if n==k:
                c+=nums[i]
        return c    
                



        