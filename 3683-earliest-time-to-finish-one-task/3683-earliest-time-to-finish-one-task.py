class Solution(object):
    def earliestTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        a=[]
        for i in range(len(tasks)):
            a.append(sum(tasks[i]))
        a.sort()    
        return a[0]

        