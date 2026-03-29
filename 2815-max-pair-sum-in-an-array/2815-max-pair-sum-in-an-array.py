class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def lar(n):
            l=0
            while n>0:
                d=n%10
                l=max(l,d)
                n=n//10
            return l    
        nums.sort(reverse=True)
        l=0
        temp=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if lar(nums[i])==lar(nums[j]):
                    temp.append(lar(nums[i]))
                    temp.append(lar(nums[j]))
                    l=max(nums[i]+nums[j],l)
        if len(temp)<=1:
            return -1            
        return l            
        
                 



       
       