class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            if nums.count(nums[i])>1:
                res.append(int(nums[i]))
        temp=set(res)
        return list(temp)  