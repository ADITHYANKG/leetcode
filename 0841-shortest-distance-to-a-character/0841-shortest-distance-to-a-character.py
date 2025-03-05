class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res=[]
        for i in range(len(s)):
            temp=[]
            for j in range(len(s)):
                if s[j]==c:
                    d=abs(j-i)
                    temp.append(d)
            k=min(temp)  
            res.append(k)
        return res             

