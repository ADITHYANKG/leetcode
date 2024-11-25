class Solution(object):
    def countConsistentStrings(self, allowed, words):
        res=0
        
        for i in range(0,len(words)):
            c=0
            for j in range(0,len(words[i])):
                for k in range(0,len(allowed)):
                    if(words[i][j]==allowed[k]):
                                c+=1
            if c>=len(words[i]):
                res+=1
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        return res