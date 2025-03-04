class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res=""
        for i in range(0,len(s),2*k):
            res+=s[i:k+i][::-1]+s[(k+i):2*k+(i)]
        return res   

