class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==min(matrix[i])  and matrix[i][j]==max([matrix[k][j] for k in range(len(matrix))]):
                    res.append(matrix[i][j])
        return res      
               
   