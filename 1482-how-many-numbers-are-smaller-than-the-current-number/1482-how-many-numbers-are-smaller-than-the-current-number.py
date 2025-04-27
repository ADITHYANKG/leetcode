class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                if i==j:
                    continue
                elif nums[i]>nums[j]:
                    c+=1
            res.append(c)
        return res    