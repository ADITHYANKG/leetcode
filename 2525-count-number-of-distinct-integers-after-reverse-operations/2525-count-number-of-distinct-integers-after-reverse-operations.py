class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res=[]
        
        for i in range(len(nums)):
            rev=0
            n=nums[i]
            while n>0:
                rev=(rev*10)+n%10
                n=n//10
            res.append(rev)
        temp=nums+res
        return len(list(set(temp)))      

