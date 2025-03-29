class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        res=0
        n=num
        while num>0:
            d=num%10
            res=(res*10)+d
            num=num//10
        # return n    
        if len(str(res))==len(str(n)):
            return True
        else:return False     

