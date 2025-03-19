class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        f=0
        allowed=list(allowed)
        for i in range(len(words)):
            c=0
            for j in range(len(words[i])):
                if words[i][j] in allowed:
                    c+=1
            if c==len(words[i]):  
                f+=1 

        return f            