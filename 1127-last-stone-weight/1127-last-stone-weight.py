class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        
        while len(stones)>1:
            
            l=len(stones)-1
            if stones[l]==stones[l-1]:
                stones.pop()
                stones.pop()
                if len(stones)==0:
                    return 0
            else :
                x= stones[l-1]
                stones[l]=stones[l]-x
                stones.pop(l-1)
            stones.sort()    

        return stones[0]