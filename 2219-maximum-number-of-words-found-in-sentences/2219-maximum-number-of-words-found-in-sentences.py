class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        big=0
        for i in range(len(sentences)):
            if len(sentences[i].split(" "))>big:
                big=len(sentences[i].split(" "))
            else:

                big=big
        return big        

        
        