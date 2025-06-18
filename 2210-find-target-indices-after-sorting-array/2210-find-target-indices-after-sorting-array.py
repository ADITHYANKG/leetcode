class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tar=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                tar.append(i)
        return tar        