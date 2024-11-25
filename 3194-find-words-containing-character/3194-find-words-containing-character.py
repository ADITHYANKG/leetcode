class Solution(object):
    def findWordsContaining(self, words, x):
        """for i in range()
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        res=[]
        for i in range(0,len(words)):
            if(words[i].count(x)>0):
                    res.append(i)
        return res 