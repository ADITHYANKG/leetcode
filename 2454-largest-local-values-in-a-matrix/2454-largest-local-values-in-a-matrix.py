class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        for i in range(0,len(grid)-2):
            tm=[]
        
            for j in range(len(grid)-2):
                t1=grid[i][j:j+3]
                t2=grid[i+1][j:j+3]
                t3=grid[i+2][j:j+3]
                temp=t1+t2+t3
                tm.append(max(temp))    
            res.append(tm)
        return res