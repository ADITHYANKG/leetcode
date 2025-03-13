class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        h=len(s)//2
        a=s[0:h]
        b=s[h:len(s)]
        c1=0
        c2=0
        for i in range(len(a)):
            if a[i] in "aeiouAEIOU":
                c1+=1

        for i in range(len(b)):
            if b[i] in "aeiouAEIOU":
                c2+=1   
        if c1==c2:
            return True
        else:
            return False