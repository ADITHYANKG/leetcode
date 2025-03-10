class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        b=bin(n)
        b=str(b)
        e=0
        o=0
        for i in range(len(b)-1,0,-1):
            if (len(b)-1-i)%2==0 and b[i]=="1":
                e+=1
            elif (len(b)-1-i)!=0 and b[i]=="1":
                o+=1
        res=[e,o]        
        return res

