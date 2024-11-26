class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def conert(n,b):
            c=""
            while n>0:
                d=str(n%b)
                c+=d
                n=n//b
            return c
        b=n-2  
        state=True  
        while b>=2:
            if conert(n,b)!=conert(n,b)[::-1]:
                     state=False
            b=b-1

        return state    