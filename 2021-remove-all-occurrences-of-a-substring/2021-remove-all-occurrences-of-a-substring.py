class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        l=len(part)
        print("l=",l)
        print(part in s)
        temp=s
        while part in s:
            for i in range(len(s)-(l-1)):
                print("i=",i)
                print(s[i:i+l])
                
                if s[i:i+l]==part:
                    temp=s[0:i]+s[i+l:len(s)]
                    s=temp
                    print("temp",temp)
                    break
        return s

       

        