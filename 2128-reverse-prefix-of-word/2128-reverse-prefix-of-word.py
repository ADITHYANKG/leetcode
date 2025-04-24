class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        l=list(word)
        
        if ch in l:
            i=l.index(ch)
            rev=word[0:i+1]
            res=rev[::-1]+word[i+1:len(word)]
            return res
        else:
            return word
       