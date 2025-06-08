class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        k=2**(len(nums[0]))
        for i in range(k):
            t=str(bin(i))
            t=t[2::]

            g=t+str("0"*(len(nums[0])-len(t)))
            if g not in nums:
                return g

        