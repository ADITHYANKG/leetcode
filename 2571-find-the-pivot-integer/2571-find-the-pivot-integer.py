class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        
        for i in range(0,n):
            s1=0
            s2=0
            for j in range(1,i+1):
                s1+=j
            for k in range(i,n+1):
                s2+=k
            if s1==s2:
                return i        
        return -1        