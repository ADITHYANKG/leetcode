class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        res=[]
        for i in range(len(accounts)):
            res.append(sum(accounts[i]))
        return max(res)    