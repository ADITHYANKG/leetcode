class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                res|=nums[i]
        return res        
