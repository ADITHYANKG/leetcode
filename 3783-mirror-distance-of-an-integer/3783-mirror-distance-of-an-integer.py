class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        r=0
        num=n
        while num>0:
            d=num%10
            r=(r*10+d)
            num=num//10

        return abs(n-r)  
