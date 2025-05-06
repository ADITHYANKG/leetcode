class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]
        for i in range(left,right+1):
            k=i
            fl=True
            while k>0:
                d=k%10
                k=k//10
                if d==0:
                    fl=False
                    break
                if i%d!=0:
                    fl=False
                    break
            if fl:
                res.append(i)        
        return res    
