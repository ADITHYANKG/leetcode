class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        for j in range(len(heights)):
            for i in range(0,len(heights)-j-1):
                if heights[i]<heights[i+1]:
                    heights[i],heights[i+1]=heights[i+1],heights[i]
                    names[i],names[i+1]=names[i+1],names[i]
        return names           
