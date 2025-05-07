class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res=[0]
        for i in range(0,len(gain)):
            res.append(res[i]+gain[i])  
        return max(res)       