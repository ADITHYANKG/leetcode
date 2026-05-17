class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel=['a','e','i','o','u']
        v=[]
        n=[]
        for c in s:
            if c.lower() in vowel:
                v.append(c)
            else:
                n.append(c)   
        v=v[::-1]   
        out=""      
        i=0
        for c in s:
            if c.lower() in vowel:
                out+=v[i]
                i+=1
            else:
                out+=c
        return out            
