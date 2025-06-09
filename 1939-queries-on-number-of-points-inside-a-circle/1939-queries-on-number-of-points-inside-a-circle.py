class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        import math
        for k in range(len(queries)):
            c=0
            for i in range(len(points)):
                d1=(points[i][0]-queries[k][0])**2
                d2=(points[i][1]-queries[k][1])**2
                D=math.sqrt((d1+d2))
                
                if D<=queries[k][2]:
                    c+=1
            res.append(c)
          

                
        return res


        