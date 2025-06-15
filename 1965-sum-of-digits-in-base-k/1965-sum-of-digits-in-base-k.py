class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res=""
        a=0
        while n>0:
            a+=n%k
            
            n=n//k
        return a
        