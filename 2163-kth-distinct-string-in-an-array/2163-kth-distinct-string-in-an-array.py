class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """

        d=[]
        for i in range(len(arr)):
            if arr.count(arr[i])==1:
                d.append(arr[i])







        if len(d)<k:
            return ""
        else:
            return d[k-1]

        
        