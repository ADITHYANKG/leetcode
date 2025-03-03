class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        c=0
        for i in range(0,len(patterns)):
            for j in range(len(word)-len(patterns[i])+1):
                if word[j:len(patterns[i])+j]==patterns[i]:
                    c+=1
                    break
        return c            

