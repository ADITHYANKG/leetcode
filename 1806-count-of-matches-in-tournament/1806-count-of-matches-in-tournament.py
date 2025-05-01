class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=0
        while n>1:
            if n%2==0:
                m+=n/2
                
            else:
                m+=(n/2)+1
            n=n//2
              
        return m
           
