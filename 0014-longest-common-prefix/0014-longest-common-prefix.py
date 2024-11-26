class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res=""
        if(len(strs)==1):
            return strs[0]
        for i in range(0,len(strs[0])):
            c=0
            
            for j in range(1,len(strs)):
                if(strs[0][0:i+1]==strs[j][0:i+1]):
                    c+=1
            if(c==(len(strs)-1)):
                res=strs[0][0:i+1]
        return res      