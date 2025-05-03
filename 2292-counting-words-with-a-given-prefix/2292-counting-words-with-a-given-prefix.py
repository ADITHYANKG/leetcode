class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        c=0
        k=len(pref)
        for i in range(len(words)):
            if words[i][0:k]==pref:
                c+=1
        return c        