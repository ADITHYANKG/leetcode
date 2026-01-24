class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        s=0
        # print(len(grid))
        while len(grid[0])>0:
            # print("--------------------")
            a=[]
            for i in range(len(grid)):
                grid[i].sort()
                # print(grid[i][-1])
                a.append(grid[i][-1])
                grid[i].pop()
            # print("a=",a)    
            s+=max(a)   
            # print("s=",s)
            # print("len after pop=",len(grid[0]))
        return s  










        