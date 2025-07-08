class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        s=0
        c=capacity
        for i in range(len(plants)):
            if c>=plants[i]:
                c-=plants[i]
                s+=1
            else:
                c=capacity
                s+=(i+1)+i
                c-=plants[i]
        return s        


    
