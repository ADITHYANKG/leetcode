class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res=[]
        temp=[0]
        sp=nums
        while len(nums)>0:
        
            temp=[0]
            sp=[x for x in sp if x!="x"]
            nums=sp
            for i in range(len(sp)):
            
                if sp[i] in temp:
                    continue
                temp.append(sp[i])
                
                sp[i]="x" 
                
            res.append(temp[1:len(temp)])  
            res=[x for x in res if x!=[]]
        return res   