class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        res=0
        for i in range(n):
            x=start+2*i
            res=res^x

        return  res    

        