class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(0,len(A)):
            a=set(A[0:i+1])
            b=set(B[0:i+1])
            c=a&b
            res.append(len(c))
        return res    

