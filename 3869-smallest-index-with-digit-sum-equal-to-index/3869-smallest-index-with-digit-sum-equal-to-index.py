class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            k=nums[i]
            d=0
            while k>0:
                d=d+(k%10)
                k=k//10
            if d==i:
                return i
                break    



        return -1