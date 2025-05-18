class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        v=['a','e','i','o','u']
        a1=[0]
        a2=[0]

        for i in range(len(s)):
            if s[i] in v:
                a1.append(s.count(s[i]))
            else:
                a2.append(s.count(s[i]))
        return max(a1)+max(a2)            

        