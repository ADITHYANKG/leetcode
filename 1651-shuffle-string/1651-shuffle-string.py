class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=[0 for x in range(len(s))]
        for i in range(len(s)):
            res[indices[i]]=s[i]
        return "".join(res)    