class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]
        for car in s:
            if car=="*":
                if l:
                    l.pop()
            else:
                l.append(car)        

        return "".join(l)
