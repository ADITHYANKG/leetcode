class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        res=""
        for i in range(len(words)):
            if words[i]==words[i][::-1]:
                return words[i]
                break
        return res        

        