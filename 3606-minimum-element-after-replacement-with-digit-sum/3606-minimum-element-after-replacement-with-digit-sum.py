class Solution:
    def minElement(self, nums: List[int]) -> int:
        res=[]
        for i in range(len(nums)):
            d=0
            while nums[i]>0:
                d+=nums[i]%10
                nums[i]//=10
            res.append(d)
        return min(res)        
