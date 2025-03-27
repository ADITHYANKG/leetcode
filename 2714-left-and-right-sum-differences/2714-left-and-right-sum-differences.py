class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            l=sum(nums[0:i])
            r=sum(nums[i+1:len(nums)])
            res.append(abs(l-r))
        return res 
