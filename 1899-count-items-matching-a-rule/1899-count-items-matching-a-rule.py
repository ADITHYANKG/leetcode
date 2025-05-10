class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        if ruleKey=="type":
            j=0
        elif ruleKey=="color":
            j=1
        else:
            j=2       
        c=0      
        for i in range(len(items)):
            if items[i][j]==ruleValue:
                c+=1
        return c        

        